from django.core.mail import mail_admins
from django.template import Context
from django.template.loader import get_template


class Reporter(object):
    def __init__(self, subject, template, base_context=None, committer=None):
        self.subject = subject
        self.template = template
        self.stored_text = []
        self.base_context = base_context if base_context is not None else {}
        self.comitter = committer if committer is not None else admin_mail_comitter

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()

    def append(self, text):
        """ Adding a line
        """
        self.stored_text.append(text)

    def extend(self, text_list):
        """ Adding multiple lines
        """
        self.stored_text.extend(text_list)

    def render(self):
        """ Render the text for getting report text
        """
        ctx = self.base_context.copy()
        ctx['stored_text'] = self.stored_text
        return get_template(self.template).render(Context(ctx))

    def commit(self):
        """ A interface to send the report
        """
        self.comitter(self.subject, self.render())


def console_comitter(subject, body):
    print(subject)
    print(body)


def admin_mail_comitter(subject, body):
    mail_admins(subject, body, fail_silently=True)
