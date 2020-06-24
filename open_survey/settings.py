"""
Django settings for open_survey project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = []

ON_HEROKU = os.getenv("ON_HEROKU", "False").lower() == "true"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openhumans',
    'main'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middleware.LoginLangMiddleware'
]

ROOT_URLCONF = 'open_survey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'open_survey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
  ('en', _('English')),
  ('fr', _('French')),
]

LOCALE_PATHS = (
    'locale',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "managedfiles")
MEDIA_URL = "/files/"

# Open Humans configuration

OPENHUMANS_APP_BASE_URL = os.getenv("OPENHUMANS_APP_BASE_URL", "http://localhost:5000")
OPENHUMANS_CLIENT_ID = os.getenv("OPENHUMANS_CLIENT_ID", "your_client_id")
OPENHUMANS_CLIENT_SECRET = os.getenv("OPENHUMANS_CLIENT_SECRET", "your_client_secret")

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# OC user for adding new participants & scheduling events
OPENCLINICA_SITE_USERNAME = os.getenv("OPENCLINICA_USERNAME", "OPENCLINICA_TOKEN")
OPENCLINICA_SITE_PASSWORD = os.getenv("OPENCLINICA_PASSWORD", "OPENCLINICA_TOKEN")

# OC user for exporting data from participants
OPENCLINICA_DATA_USERNAME = os.getenv("OPENCLINICA_DATA_USERNAME", "OPENCLINICA_TOKEN")
OPENCLINICA_DATA_PASSWORD = os.getenv("OPENCLINICA_DATA_PASSWORD", "OPENCLINICA_TOKEN")


OPENCLINICA_STUDY = os.getenv("OPENCLINICA_STUDY", "OPENCLINICA_STUDY ")

OPENCLINICA_SITE = os.getenv("OPENCLINICA_SITE", "OPENCLINICA_SITE")

OPENCLINICA_PARTICIPATE_LINK = os.getenv("OPENCLINICA_PARTICIPATE_LINK", "OPENCLINICA_PARTICIPATE_LINK")


if ON_HEROKU:
    django_heroku.settings(locals())


REMOTE = os.getenv("REMOTE")
if REMOTE:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
