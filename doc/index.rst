Welcome to django-password-validation!
======================================

A backport of the `password validation system`_ from Django 1.9 (by Erik
Romijn), for use on earlier Django versions.

Password validation isn't hard to implement yourself, but if you use this
backport you'll be writing your validators to the same API that will be
built-in to upcoming Django versions.

.. _password validation system: https://docs.djangoproject.com/en/dev/topics/auth/passwords/#password-validation


Prerequisites
-------------

``django-password-validation`` supports `Django`_ 1.8.2 and later on Python
2.7, 3.3, 3.4, pypy, and pypy3.

.. _Django: http://www.djangoproject.com/


Installation
------------

``django-password-validation`` is available on `PyPI`_. Install it with::

    pip install django-password-validation

.. _PyPI: https://pypi.python.org/pypi/django-password-validation/


Usage
-----

Just follow the `Django documentation`_!

When using the built-in validators in your ``AUTH_PASSWORD_VALIDATORS``
setting, use import paths like
e.g. ``'password_validation.MinimumLengthValidator'`` in place of
``'django.contrib.auth.password_validation.MinimumLengthValidator'``.

In place of the built-in views for password setting/changing you'll need to
switch to using ``password_validation.views.password_reset`` and
``password_validation.views.password_change``.

If you have your own custom views for changing or resetting passwords, use
``password_validation.forms.SetPasswordForm`` or
``password_validation.forms.PasswordChangeForm`` instead of
``django.contrib.auth.forms.SetPasswordForm`` or
``django.contrib.auth.forms.PasswordChangeForm`` in those views.

A validation-enabled admin password change form is not currently provided
here. Pull requests welcome!

.. _django documentation: https://docs.djangoproject.com/en/dev/topics/auth/passwords/#password-validation


Contributing
------------

See the `contributing docs`_.

.. _contributing docs: https://github.com/orcasgit/django-password-validation/blob/master/CONTRIBUTING.rst
