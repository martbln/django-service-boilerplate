"""
Django settings for _project_ project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
BASE_DIR_NAME = os.path.basename(BASE_DIR)
DATA_DIR = os.path.join(BASE_DIR, '__data__')

REDIS_HOST = '127.0.0.1'
POSTGRES_HOST = '127.0.0.1'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0n-w7wsf^3-ehi^!@m2fayppf7cc3k4j5$2($59ai*5whm^l7k'  # noqa: dodgy: secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# ------------------ #
# --- <SERVICES> --- #

# SENTRY
RAVEN_CONFIG = {
    'dsn': '',
}

# DATABASE
DATABASE_NAME = BASE_DIR_NAME
DATABASE_HOST = POSTGRES_HOST
DATABASE_USER = None
DATABASE_PASSWORD = None

# CACHE
CACHE_KEY_PREFIX = BASE_DIR_NAME
CACHE_HOST = REDIS_HOST

# --- </SERVICES> --- #
# ------------------- #

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # CELERY
    'django_celery_results',

    # SENTRY
    'raven.contrib.django.raven_compat',

    # DEV
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # DEV
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

WSGI_APPLICATION = '_project_.wsgi.application'
ROOT_URLCONF = '_project_.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': '5432'
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + CACHE_HOST + ":6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": CACHE_KEY_PREFIX
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.'
             'UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'  # 'ru-RU'

TIME_ZONE = 'UTC'  # 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(DATA_DIR, 'static'))
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(DATA_DIR, 'media'))

# Celery
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = "redis://" + REDIS_HOST + ":6379/0"
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']  # Ignore other content
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 3600
CELERYBEAT_SCHEDULE_FILENAME = os.path.join(DATA_DIR, 'celerybeat.db')
CELERYBEAT_SCHEDULE = {}

try:
    from .settings_local import *  # noqa: pylint: unused-wildcard-import, pylint: wildcard-import
except ImportError:
    pass
