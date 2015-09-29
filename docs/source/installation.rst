Installation
============

Won't you know about django-reportmail? Continue to read following documentation!
If you do, you will learn the way to setup django-reportmail.

How to install
--------------

As always, you can install django-reportmail by using `pip`::

    pip install django-reportmail

And then, you need to fix 2 parts of `settings.py`.
First, Add a line 'reportmail' to INSTALLED_APPS to register this library for your project:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'reportmail',
    )


And also you need to set 'ADMINS' settings.
Because this library will send the report mail to 'ADMINS' on settings.

.. code-block:: python

    ADMINS = (
        ('Hiroki KIYOHARA', 'hirokiky@gmail.com'),
    )

    SERVER_EMAIL = 'noreply@example.com'

Internally, the reason of setting 'ADMINS' and 'SERVER_EMAIL' is that django-reportmail
will send mail by calling `django.core.mail.mail_admins()`.
For more detail, please check out the official documentation about `mail_admins`.
https://docs.djangoproject.com/en/1.6/topics/email/#mail-admins

Requires
--------

django-reportmail is guaranteed to work correctly on following environments.

Python:

* 2.7
* 3.3
* 3.4
* 3.5

Django:

* 1.6
* 1.7
* 1.8

All set
-------

After setting up the project, you can head over to the :doc:`intro` documentation!
