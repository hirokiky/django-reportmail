Getting started
===============

Won't you know about django-reportmail?
Continue to read following documentation!

How to install
--------------

Install django-reportmail
^^^^^^^^^^^^^^^^^^^^^^^^^
::

    pip install django-reportmail

How to setup
^^^^^^^^^^^^

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


Requires
^^^^^^^^

Python:

* 2.7
* 3.3

Django:

* 1.6

How to use
----------

Basic usage
^^^^^^^^^^^

Processing flow
^^^^^^^^^^^^^^^

What will be happened when unexpected error occurred
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
