from functools import wraps
import traceback

from reportmail.reporter import AdminEmailReporter


def apply_reporter(subject, template='reportmail/command_report.txt'):
    """ Adding a reporting feature for django command

    You can use thin as decorator for Command.handle.
    and decorated handle() will get admin mail reporter objects as first argument::

        @reporter("Title of report", 'path/to/template.txt')
        def handle(reporter, *args, **options):
            ...

    * :arg subject: Title of report
    * :arg template: Template to use rendering
    """
    def wrapper(handle_func):
        @wraps(handle_func)
        def wrapped(self, *args, **options):
            with AdminEmailReporter(subject, template,
                                    base_context={'args': args, 'options': options,
                                                  'command': self.__module__}) as reporter:
                try:
                    ret = handle_func(self, reporter, *args, **options)
                except Exception as e:
                    reporter.append(str(e) + '\n\n' + traceback.format_exc())
                    raise
            return ret
        return wrapped
    return wrapper
