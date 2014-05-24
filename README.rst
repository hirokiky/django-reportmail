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
        Report of someapp.management.commands.some_of_your_command
        args: path/to/somecsv.csv
        options:

        result:
        Line1: processed {'somefield': 'somevalue0'}
        Line2: processed {'somefield': 'somevalue1'}
        Line3: processed {'somefield': 'somevalue2'}
        Line4: processed {'somefield': 'somevalue3'}
        ...


Required settings
=================

First, Add a line 'reportmail' to INSTALLEDAPPS to register this library for your project:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'reportmail',
    )


And also you need to set 'ADMINS' settings.
Because the above 'apply_reporter' will send the report mail to ADMINS on settings.

.. code-block:: python

    ADMINS = (
        ('Hiroki KIYOHARA', 'hirokiky@gmail.com'),
    )


Versions
========

Python:

* 2.7
* 3.3

Django:

* 1.6

Resources
=========

* `Github <https://github.com/hirokiky/django-reportmail/>`_
* `PyPI <http://pypi.python.org/pypi/django-reportmail>`_
