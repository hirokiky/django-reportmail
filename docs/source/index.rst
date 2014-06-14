Welcome to django-reportmail
============================

Welcome to django-reportmail's documentation.
django-reportmail is a django library to send 'report' mail.
Almost django management commands used as night batch processing,
and then, administrators will want to know the result as mail.
If you want to notice results of some django commands, stick with this doc and try django-reportmail.

I recommend that you get started with :doc:`installation` and then head over to the :doc:`intro`.

Why django-reportmail
---------------------

Of Cause, you can emit logs and aggregate them by using some another applications like Sentry.
But in some cases, you can't deploy them and you should send the report as mail.

A situation like that, django-reportmail will be really helpful for you.

Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   intro
   advanced
   api

Resources
---------

* `Documentation <http://django-reportmail.readthedocs.org/>`_
* `Github <https://github.com/hirokiky/django-reportmail/>`_
* `PyPI <http://pypi.python.org/pypi/django-reportmail>`_
