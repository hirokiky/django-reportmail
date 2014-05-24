=================
django-reportmail
=================

Django library to send 'report' mail.

Almost django management commands used as night batch processing,
and then, administrators will want to know the result of it as mail.

Why django-reportmail
=====================

Of Cause, you can emit logs and aggregate them by using some another applications like Sentry.
But in some cases, you can't deploy them and you should send the report as mail.

Usage
=====

.. code-block:: python

    import csv
    from django.core.management.base import BaseCommand

    from reportmail.command import apply_reporter

    class Command(BaseCommand):
        @apply_reporter("Title")
        def handle(reporter, filepath, *args, **options):
            for i, l in enumerate(csv.DictReader(open(filepath))):
                reporter.append('Line {}: processed {l}'.format(i+1, l))


Then, when the command finish, you'll get a admin mail like this::

    Subject:
        Title
    Body:
        Line1: processed {'somefield': 'somevalue0'}
        Line2: processed {'somefield': 'somevalue1'}
        Line3: processed {'somefield': 'somevalue2'}
        Line4: processed {'somefield': 'somevalue3'}
        ...

