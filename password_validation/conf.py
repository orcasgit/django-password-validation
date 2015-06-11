from django.conf import settings as django_settings


class SettingsProxy(object):
    @property
    def AUTH_PASSWORD_VALIDATORS(self):
        return getattr(django_settings, 'AUTH_PASSWORD_VALIDATORS', [])


settings = SettingsProxy()
