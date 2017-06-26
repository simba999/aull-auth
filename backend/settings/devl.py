import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'NAME': 'simpleone',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}

INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # add allauth component
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4',
    },
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },
}
