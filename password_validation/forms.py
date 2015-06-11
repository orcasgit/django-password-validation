from django.contrib.auth import forms

from . import validation


class SetPasswordForm(forms.SetPasswordForm):
    def __init__(self, *a, **kw):
        super(SetPasswordForm, self).__init__(*a, **kw)
        self.fields['new_password1'].help_text = validation.password_validators_help_text_html()

    def clean_new_password2(self):
        password = super(SetPasswordForm, self).clean_new_password2()
        validation.validate_password(password, self.user)

    def save(self, commit=True):
        user = super(SetPasswordForm, self).save(commit=commit)
        validation.password_changed(self.cleaned_data['new_password1'], user)
        return user
