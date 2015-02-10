"""
Django settings for resume project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Parse database configuration from $DATABASE_URL
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Parse database configuration from $DATABASE_URL
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# The minimum value for the password
MIN_VAL_PASS = 6

# The maximum value for the password
MAX_VAL_PASS = 16

# email settings
# please, set here you smtp server details and your admin email
DEFAULT_FROM_EMAIL = 'artgrem@gmail.com'

MANAGERS = (
    ('Grigoriy GMAIL', 'artgrem@gmail.com'),
)

# MANDRILL MAIL
ADMIN_EMAIL = 'artgrem@gmail.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'artgrem@gmail.com'
EMAIL_HOST_PASSWORD = 'tsdLAQQ9lAbrvYwn5V8PRA'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q_bl3ylg%4m0$bkunltvfeo5w%_vj+1k3d+5hc10l0%55pu)d1'

# Salt Key
SALT_KEY = '1this_2user_3is_4a_5valid'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PORTAL_URL = 'http://localhost:8000'

# TEMPLATE_CONTEXT_PROCESSORS
from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "resume.context_processor.absoluteResumeUrl",
    "resume.context_processor.activePage",
    "resume.context_processor.pathToPhoto",
    )

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrap3_datetime',
    'resumeapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'resume.urls'

WSGI_APPLICATION = 'resume.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CRISPY_CLASS_CONVERTERS = {'dateinput form-control': "glyphicon glyphicon-calendar"}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Database settings for production server
# import sys
# sys.path.insert(0, os.path.join(BASE_DIR, '..'))
# import settings_db

# DATABASES = settings_db.dataDb()

# Database settings for debug
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_postgrespool',
#         'HOST': 'ec2-174-129-213-103.compute-1.amazonaws.com',
#         'USER': 'rbfrtnwxyfgtfn',
#         'PASSWORD': 'Fd-_Va27VPHTumBqecpZc3IyIY',
#         'NAME': 'd6o2soljsnsmmk',
#     }
# }

# Parse database configuration from $DATABASE_URL
DATABASES = {'default': dj_database_url.parse('postgres://idrloqqyryhicb:6IWDaN2u2A1i4GU0vkI-5fRRGk@ec2-54-83-204-78.compute-1.amazonaws.com:5432/d1e6s0pjd8nalu')}
# DATABASES['default'] =  dj_database_url.config('postgres://rbfrtnwxyfgtfn:Fd-_Va27VPHTumBqecpZc3IyIY@ec2-174-129-213-103.compute-1.amazonaws.com:5432/d6o2soljsnsmmk')
HEROKU_POSTGRESQL_OLIVE_URL = 'postgres://idrloqqyryhicb:6IWDaN2u2A1i4GU0vkI-5fRRGk@ec2-54-83-204-78.compute-1.amazonaws.com:5432/d1e6s0pjd8nalu'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'



# Pool size is configurable
# DATABASE_POOL_ARGS = {
#     'max_overflow': 10,
#     'pool_size': 2,
#     'recycle': 300
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CAPTCHA settings
RECAPTCHA_PUBLIC_KEY = '76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh'
RECAPTCHA_PRIVATE_KEY = '98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs'
RECAPTCHA_USE_SSL = True
CAPTCHA_AJAX = True
