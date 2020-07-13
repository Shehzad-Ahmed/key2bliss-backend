"""
Django settings for key2bliss project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import environ

env = environ.Env(
    DEBUG=(bool, False),
    USE_HTTPS_IN_RESET_PASSWORD=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    "django_extensions",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'key2bliss.api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'key2bliss.urls'

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

WSGI_APPLICATION = 'key2bliss.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "key2bliss",
        "USER": "key2bliss",
        "PASSWORD": "key2bliss",
        "HOST": "localhost",
        "PORT": "5432",
        "TEST": {"NAME": "key2bliss_test"},
        "CONN_MAX_AGE": 0 if DEBUG else 3600,
    }
}

DATABASES = {
    "default": env.db()  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"
DATABASES["default"]["CONN_MAX_AGE"] = 0 if DEBUG else 3600
DATABASES["default"]["TEST"] = {"NAME": env("TEST_DATABASE_NAME")}

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",

    )
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = env("EMAIL_HOST")

EMAIL_PORT = env("EMAIL_PORT")

EMAIL_HOST_USER = env("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

EMAIL_USE_TLS = False

EMAIL_USE_SSL = True

AUTH_USER_MODEL = "api.Users"

USE_HTTPS_IN_RESET_PASSWORD = env("USE_HTTPS_IN_RESET_PASSWORD")
