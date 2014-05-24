from testfixtures import OutputCapture

from django.test import TestCase
from django.test.utils import override_settings


class TestReporter(TestCase):
    def _getTarget(self):
        from reportmail.reporter import Reporter
        return Reporter

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__append(self):
        target = self._makeOne("", '')
        target.append('stored text')
        self.assertEqual(target.stored_text, ['stored text'])

    def test__extend(self):
        target = self._makeOne("", '')
        target.extend(['stored text 1', 'stored text 2'])
        self.assertEqual(target.stored_text, ['stored text 1', 'stored text 2'])

    def test__render(self):
        target = self._makeOne("", 'reportmail/report.txt')
        target.stored_text = ["test1", "test2"]
        target.base_context['additional'] = 'additional'
        actual = target.render()
        self.assertEqual(actual, "test1\ntest2\n\nadditional\n")


class TestConsoleReporter(TestReporter):
    def _getTarget(self):
        from reportmail.reporter import ConsoleReporter
        return ConsoleReporter

    def test__commit(self):
        target = self._makeOne("Console", 'reportmail/report.txt')
        target.append("This is test 1")
        target.append("This is test 2")

        with OutputCapture() as output:
            target.commit()

        output.compare("""\
Console
This is test 1
This is test 2


""")


class TestAdminEmailReporter(TestReporter):
    def _getTarget(self):
        from reportmail.reporter import AdminEmailReporter
        return AdminEmailReporter

    @override_settings(SERVER_EMAIL='server@example.com',
                       ADMINS=(('Admin', 'admin@example.com'),),
                       EMAIL_SUBJECT_PREFIX="")
    def test__commit(self):
        target = self._makeOne("Admin mail", 'reportmail/report.txt')
        target.append("This is test 1")
        target.append("This is test 2")
        target.commit()

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, 'server@example.com')
        self.assertEqual(mail.outbox[0].to, ['admin@example.com'])
        self.assertEqual(mail.outbox[0].subject, "Admin mail")
        self.assertEqual(mail.outbox[0].body, "This is test 1\nThis is test 2\n\n\n")
