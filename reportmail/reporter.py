"""

A module for reporting.

.. autosummary::

    Reporter
    console_committer
    admin_mail_committer
    manager_mail_committer

`Committers` is callable to make some side-effect telling result message for administrators.
Internally Reporter uses Committer to tell messages.
So committers are totally separated from reporters and reporter delegates the sending processing to
committers.
"""
from django.core.mail import mail_admins, mail_managers
from django.template import Context
from django.template.loader import get_template


class Reporter(object):
    """ An object to store result messages and send messages by using committer.

    The API of Reporter is quite simple. You can store messages as same way as list, like this:

    >>> reporter = Reporter()
    >>> reporter.append("The first line")
    >>> reporter.append("The second line")
    >>> reporter.commit()

    When the `commit()` method is called, stored messages will be sent to administrators.
    You can also use committer as a context manager.
    If you do, you won't need to call `commit()` method explicitly.

    >>> with Reporter() as reporter:
    >>>     reporter.append("The first line")
    >>>     reporter.append("The second line")

    This way is better and easier to read. so I recommend to use Reporter as context manager.
    Notice that the reporter won't handle exceptions by default.
    If you want reporter to catch exceptions and report about it,
    write the explicit code like this:

    >>> import traceback
    >>> with Reporter() as reporter:
    >>>     try:
    >>>         # do_something()
    >>>         reporter.append("Success")
    >>>     except Exception as e:
    >>>         reporter.append(str(e) + traceback.format_exc())
    >>>         raise

    :arg str subject:
        A subject of message. This value will be deliver for committer directly.
    :arg str template:
        A string to specify a template to be used for build result message.
    :arg  dict base_context:
        Base context will be provided for the template.
        By default, empty dict will be used.
    :arg callable committer:
        Committer function.
        By default, admin_mail_committer will be used.
    """
    def __init__(self, subject, template, base_context=None, committer=None):
        self.subject = subject
        self.template = template
        self.stored_text = []
        self.base_context = base_context if base_context is not None else {}
        self.committer = committer if committer is not None else admin_mail_committer
        self.aborted = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()

    def append(self, text):
        """ Storing a line of message

        :arg str text: A string of message to store
        """
        self.stored_text.append(text)

    def extend(self, text_list):
        """ Storing some lines of messages

        :arg list text: A list of Some messages to store
        """
        self.stored_text.extend(text_list)

    def render(self):
        """ Rendering result by using stored messages

        The context for template will contain messages you stored
        as 'stored_text' value.
        And also it contains values from `base_context` of constructing.
        """
        ctx = self.base_context.copy()
        ctx['stored_text'] = self.stored_text
        return get_template(self.template).render(Context(ctx))

    def abort(self):
        self.aborted = True

    def commit(self):
        """ A interface to send the report

        Internally, this method will call `self.committer` by passing
        `self.subject and result of `self.render()`.
        """
        if not self.aborted:
            self.committer(self.subject, self.render())


def console_committer(subject, body):
    """ One of committers to send messages to standard output.

    This committer will simply output the message, separating
    subject and body by breaking.
    """
    print(subject)
    print(body)


def admin_mail_committer(subject, body):
    """ One of committers to send messages to Admin Mails.

    This committer depends on django's django.core.mail.mail_admins.
    So you need to set 'ADMINS' of the settings file.
    Notice that thin committer will fail silently to avoid
    causing unexpected error while sending admin mails.

    This committer will simply use the subject as mail subject,
    and use body as mail body.
    """
    mail_admins(subject, body, fail_silently=True)


def manager_mail_committer(subject, body):
    """ One of committers to send messages to Manager Mails.

    This committer depends on django's django.core.mail.mail_managers.
    So you need to set 'MANAGERS' of the settings file.
    Notice that thin committer will fail silently to avoid
    causing unexpected error while sending manager mails.

    This committer will simply use the subject as mail subject,
    and use body as mail body.
    """
    mail_managers(subject, body, fail_silently=True)
