from django.dispatch import receiver
from django.test.signals import setting_changed

from password_validation import get_default_password_validators


@receiver(setting_changed)
def changed_validators(**kwargs):
    if kwargs['setting'] == 'AUTH_PASSWORD_VALIDATORS':
        get_default_password_validators.cache_clear()
