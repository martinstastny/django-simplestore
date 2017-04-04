from .base import *

DEBUG = True

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'catcaves',
        'HOST': '127.0.0.1',
        'USER': '',
        'PASSWORD': '',
        'PORT': '5433'
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1'
]
