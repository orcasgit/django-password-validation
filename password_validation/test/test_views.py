from password_validation import forms, views


def mock_view(*args, **kwargs):
    return args, kwargs


def test_password_reset_confirm(monkeypatch):
    monkeypatch.setattr(views.auth_views, 'password_reset_confirm', mock_view)

    args, kwargs = views.password_reset_confirm()
    custom = object()
    args2, kwargs2 = views.password_reset_confirm(set_password_form=custom)

    assert kwargs['set_password_form'] is forms.SetPasswordForm
    assert kwargs2['set_password_form'] is custom


def test_password_change(monkeypatch):
    monkeypatch.setattr(views.auth_views, 'password_change', mock_view)

    args, kwargs = views.password_change()
    custom = object()
    args2, kwargs2 = views.password_change(password_change_form=custom)

    assert kwargs['password_change_form'] is forms.PasswordChangeForm
    assert kwargs2['password_change_form'] is custom
