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
        'NAME': 'django_simple_ecommerce',
        'HOST': '127.0.0.1',
        'USER': '',
        'PASSWORD': '',
        'PORT': '5432'
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1'
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
