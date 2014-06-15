from django.test import TestCase
from django.test.utils import override_settings


@override_settings(ADMINS=(('admin', 'admin@example.com'),),
                   EMAIL_SUBJECT_PREFIX="")
class TestApplyReporter(TestCase):
    def _makeOne(self, *args):
        from reportmail.command import apply_reporter
        return apply_reporter(*args)

    def test__it(self):
        class DummySelf(object):
            __module__ = '__module__'
        wrapper = self._makeOne("Title")

        def wrapped(self, reporter, *args, **options):
            reporter.append("Stored")
            return reporter, args, options

        r, a, o = wrapper(wrapped)(DummySelf(), 'arg', test='option')
        self.assertEqual(r.subject, "Title")
        self.assertEqual(r.template, 'reportmail/command_report.txt')
        self.assertEqual(r.base_context, {'args': a, 'options': o,
                                          'command': '__module__'})
        self.assertEqual(r.stored_text, ["Stored"])
        self.assertEqual(a, ('arg',))
        self.assertEqual(o, {'test': 'option'})

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Title')
        self.assertEqual(mail.outbox[0].body, """\
Report of __module__
args: arg,
options: test=option,

result:
Stored
""")

    def test__unexpected_error_occurred(self):
        class DummySelf(object):
            __module__ = '__module__'

        wrapper = self._makeOne("Title")

        def wrapped(self, reporter, *args, **options):
            reporter.append("Stored")
            raise Exception("KADOOOOM!!!!!")

        with self.assertRaises(Exception):
            wrapper(wrapped)(DummySelf(), 'arg', test='option')

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Title')
        self.assertEqual(mail.outbox[0].body[:120], """\
Report of __module__
args: arg,
options: test=option,

result:
Stored
KADOOOOM!!!!!

Traceback (most recent call last):
""")
