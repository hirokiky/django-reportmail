from django.test import TestCase
from django.test.utils import override_settings


class TestReporter(TestCase):
    def _makeOne(self, *args):
        from reportmail.command import apply_reporter
        return apply_reporter(*args)

    @override_settings(ADMINS=(('admin', 'admin@example.com'),))
    def test__it(self):
        wrapper = self._makeOne("Title", 'reportmail/test/report.txt')

        def wrapped(self, reporter, *args, **options):
            reporter.append("Stored")
            return self, reporter, args, options

        s, r, a, o = wrapper(wrapped)('self', 'arg', test='option')
        self.assertEqual(s, 'self')
        self.assertEqual(r.subject, "Title")
        self.assertEqual(r.template, 'reportmail/test/report.txt')
        self.assertEqual(r.base_context, {'args': a, 'options': o})
        self.assertEqual(r.stored_text, ["Stored"])
        self.assertEqual(a, ('arg',))
        self.assertEqual(o, {'test': 'option'})

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
