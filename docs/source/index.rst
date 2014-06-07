Welcome to django-reportmail
============================

Welcome to django-reportmail's documentation.
django-reportmail is a django library to send 'report' mail.

Almost django management commands used as night batch processing,
and then, administrators will want to know the result of it as mail.

Why django-reportmail
=====================

Of Cause, you can emit logs and aggregate them by using some another applications like Sentry.
But in some cases, you can't deploy them and you should send the report as mail.

At a glance
-----------

Using django-reportmail is not so difficult.
It requires you to write the code decorating the handle method
by `reportmail.command.apply_reporter`. like this:

.. code-block:: python

    import csv
    from django.core.management.base import BaseCommand

    from reportmail.command import apply_reporter

    class Command(BaseCommand):
        @apply_reporter("Title")
        def handle(reporter, filepath, *args, **options):
            for i, l in enumerate(csv.DictReader(open(filepath))):
                reporter.append('Line {}: processed {l}'.format(i+1, l))


Then, when the above command finish, you'll get a admin mail like this::

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

If you prefer this django-reportmail, go to :doc:`intro` page
and learn how to to install, setup and way to use for detail.

Resources
---------

* `Documentation <http://django-reportmail.readthedocs.org/>`_
* `Github <https://github.com/hirokiky/django-reportmail/>`_
* `PyPI <http://pypi.python.org/pypi/django-reportmail>`_

Contents
--------

.. toctree::
   :maxdepth: 3

   intro
   advanced
