=================
django-reportmail
=================

Django library to send 'report' mail.

Almost django management commands used as night batch processing,
and then, administrators will want to know the result of it as mail.

At a glance
===========

Consider a case which is for processing lines of csv by django's management command.
And then you want to know the result of the command by mail.

Just thing you should do is decorating `handle` method by `apply_reporter` method:

.. code-block:: python

    import csv
    from django.core.management.base import BaseCommand

    from reportmail.command import apply_reporter

    class Command(BaseCommand):
        @apply_reporter("Title")
        def handle(reporter, filepath, *args, **options):
            for i, l in enumerate(csv.DictReader(open(filepath))):
                reporter.append('Line {}: processed {}'.format(i+1, l))


Then, when the command finish, you'll get a admin mail like this::

    Subject:
        Title
    Body:
        Report of someapp.management.commands.some_of_your_command
        args: path/to/somecsv.csv
        options: settings=None,pythonpath=None,traceback=None,verbosity=1,

        result:
        Line1: processed {'somefield': 'somevalue0'}
        Line2: processed {'somefield': 'somevalue1'}
        Line3: processed {'somefield': 'somevalue2'}
        Line4: processed {'somefield': 'somevalue3'}
        ...

If you like django-reportmail, please refer `the documentation <http://django-reportmail.readthedocs.org/>`_.
You can learn about django-reportmail enough to use it on your work.

Resources
=========

* `Documentation <http://django-reportmail.readthedocs.org/>`_
* `Github <https://github.com/hirokiky/django-reportmail/>`_
* `PyPI <http://pypi.python.org/pypi/django-reportmail>`_
