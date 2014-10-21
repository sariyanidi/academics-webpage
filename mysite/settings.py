"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import sys
sys.path.append(BASE_DIR+'/packages')
sys.path.append(BASE_DIR+'/packages/generic')
sys.path.append(BASE_DIR+'/lib/python2.7/site-packages')

M_TN_SIZE = 50
L_TN_SIZE = 120

M_IM_SIZE = 600

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#+oas2j(6e8n==fb2hz8(*@g-j!_c&vjb&+0br%w1r2u0z$q#n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite.blog',
    'south',
    'embed_video',
    'markdown_deux'
)

TEMPLATE_CONTEXT_PROCESSORS = (
      'django.contrib.auth.context_processors.auth',
      'django.core.context_processors.i18n',
      'django.core.context_processors.request',
      'django.contrib.messages.context_processors.messages',
      'django.core.context_processors.static',
      'mysite.processor.context_personal_settings'
)

LOCALE_PATHS = (
    BASE_DIR+'/locale',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

BASE_URL = '127.0.0.1:8000'
#BASE_URL = 'sariyanidi.pythonanywhere.com'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR+'/static/'



FILE_UPLOAD_TEMP_DIR = os.path.join(os.path.dirname(__file__), '../tmp').replace('\\','/')


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media').replace('\\','/');
MEDIA_URL = "http://"+BASE_URL+'/media/'

STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '../static_src').replace('\\','/'), MEDIA_ROOT,)

import MySQLdb

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'personal',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {
                    'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci'
        },
    }
}

