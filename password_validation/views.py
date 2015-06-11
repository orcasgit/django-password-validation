from django.contrib.auth import views as auth_views

from . import forms


def password_reset_confirm(*args, **kwargs):
    kwargs.setdefault('set_password_form', forms.SetPasswordForm)
    return auth_views.password_reset_confirm(*args, **kwargs)


def password_change(*args, **kwargs):
    kwargs.setdefault('password_change_form', forms.PasswordChangeForm)
    return auth_views.password_change(*args, **kwargs)
