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
        target = self._makeOne("", 'reportmail/test/report.txt')
        target.stored_text = ["test1", "test2"]
        target.base_context['additional'] = 'additional'
        actual = target.render()
        self.assertEqual(actual, "test1\ntest2\n\nadditional\n")

    def test__commit(self):
        self.actual_subject = None
        self.actual_body = None

        def dummy_committer(subject, body):
            self.actual_subject = subject
            self.actual_body = body

        target = self._makeOne("subject", 'reportmail/test/report.txt', committer=dummy_committer)
        target.stored_text = ["test1", "test2"]
        target.commit()
        self.assertEqual(self.actual_subject, "subject")
        self.assertEqual(self.actual_body, "test1\ntest2\n\n\n")


class TestConsoleCommitter(TestCase):
    def _callFUT(self, *args, **kwargs):
        from reportmail.reporter import console_comitter
        return console_comitter(*args, **kwargs)

    def test__commit(self):
        with OutputCapture() as output:
            self._callFUT("subject", "body")

        output.compare("""\
subject
body""")


class TestAdminMailCommitter(TestCase):
    def _callFUT(self, *args, **kwargs):
        from reportmail.reporter import admin_mail_comitter
        return admin_mail_comitter(*args, **kwargs)

    @override_settings(SERVER_EMAIL='server@example.com',
                       ADMINS=(('Admin', 'admin@example.com'),),
                       EMAIL_SUBJECT_PREFIX="")
    def test__commit(self):
        self._callFUT("Admin mail", "This is test")

        from django.core import mail
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].from_email, 'server@example.com')
        self.assertEqual(mail.outbox[0].to, ['admin@example.com'])
        self.assertEqual(mail.outbox[0].subject, "Admin mail")
        self.assertEqual(mail.outbox[0].body, "This is test")
