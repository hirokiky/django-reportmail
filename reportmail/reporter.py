from django.core.mail import mail_admins
from django.template import Context
from django.template.loader import get_template


class Reporter(object):
    def __init__(self, subject, template, base_context=None):
        self.subject = subject
        self.template = template
        self.stored_text = []
        self.base_context = base_context if base_context is not None else {}

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
        raise NotImplementedError


class ConsoleReporter(Reporter):
    def commit(self):
        print(self.subject)
        print(self.render())


class AdminEmailReporter(Reporter):
    def commit(self):
        mail_admins(self.subject, self.render(), fail_silently=True)
