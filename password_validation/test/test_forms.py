"""The test in this module is backported from Django.

Copied from tests/auth_tests/test_forms.py at commit
9851e54121b3eebd3a7a29de3ed874d82554396b

The only changes are to replace `django.contrib.auth.password_validation` with
`password_validation` throughout, and replace `User.objects.get` with
`User.objects.create`.

"""
from __future__ import unicode_literals

from password_validation.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.test import TestCase, override_settings


@override_settings(USE_TZ=False, PASSWORD_HASHERS=['django.contrib.auth.hashers.SHA1PasswordHasher'])
class SetPasswordFormTest(TestCase):
    @override_settings(AUTH_PASSWORD_VALIDATORS=[
        {'NAME': 'password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'password_validation.MinimumLengthValidator', 'OPTIONS': {
            'min_length': 12,
        }},
    ])
    def test_validates_password(self):
        user = User.objects.create(username='testclient')
        data = {
            'new_password1': 'testclient',
            'new_password2': 'testclient',
        }
        form = SetPasswordForm(user, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form["new_password2"].errors), 2)
        self.assertIn('The password is too similar to the username.', form["new_password2"].errors)
        self.assertIn(
            'This password is too short. It must contain at least 12 characters.',
            form["new_password2"].errors
        )
