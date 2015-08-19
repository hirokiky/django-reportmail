from functools import wraps
import traceback

from reportmail.reporter import Reporter


def apply_reporter(subject, template='reportmail/command_report.txt', committer=None, reporter_cls=Reporter):
    """ Adding a reporting feature for django command

    You can use this as decorator for Command.handle.
    and decorated handle() will get admin mail reporter object after `self`::

        @apply_reporter("Title of report", 'path/to/template.txt')
        def handle(self, reporter, *args, **options):
            ...

    By default, `apply_reporter` will use the `reportmail/command_report.txt` template.
    To change the template, you can put same name template.

    This decorator provide these additional values for template as context:

    * args: arguments of command calling.
    * options: option arguments of command calling and some value of enviroments.
    * command: module path for this command.

    Notice that if the decorated command raises an exception,
    It will caught it to add the traceback to report mail.
    After added the error message, raised exception will be reraised.

    :arg subject: Title of report
    :arg template: Template to use rendering
    :arg committer: Committer function to be passed for the reporter.
    """
    def wrapper(handle_func):
        @wraps(handle_func)
        def wrapped(self, *args, **options):
            with reporter_cls(subject, template,
                          base_context={'args': args, 'options': options,
                                        'command': self.__module__},
                          committer=committer) as reporter:
                try:
                    ret = handle_func(self, reporter, *args, **options)
                except Exception as e:
                    reporter.append(str(e) + '\n\n' + traceback.format_exc())
                    raise
            return ret
        return wrapped
    return wrapper
