"""
Django settings for store project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10.5/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10.5/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os , sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# Append Apps Folder to PYTHONPATH
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#x8^)n$qwo@oy8=n%hz+ukdu*awuv8z03!!tpk(_3-u56i=)17'

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'easy_thumbnails',
    'filer',
    'mptt',
    'crispy_forms',
    'storages',
    'profiles',
    'products',
    'cart',
    'checkout',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'store.urls'

WSGI_APPLICATION = 'store.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'HOST': '',
        'USER': '',
        'PASSWORD': '',
        'PORT': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10.5/topics/i18n/

LANGUAGES = [
    ('en-us', 'English'),
    # ('cs-cz', 'Czech'),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10.5/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_count_processor',
            ],
            'loaders' : [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Easy Thumbnails Settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

SITE_ID = 1

CMS_PERMISSION = True

AUTH_USER_MODEL = 'profiles.Profile'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

FILER_DEBUG = True

# Addresses Types
ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

# Orders Statuses
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('in_progress', 'In Progress'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('canceled', 'Cancelled'),
)
