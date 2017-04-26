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
#
os.environ['S3_USE_SIGV4'] = 'True'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_STORAGE_BUCKET_NAME = 'martinsteststorage'
AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_KEY')