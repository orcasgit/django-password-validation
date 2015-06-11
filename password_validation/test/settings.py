import os

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

SECRET_KEY = 'secret'

HERE = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(HERE, 'test.sqlite'),
    }
}

SILENCED_SYSTEM_CHECKS = ['1_7.W001']
