"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

New

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open('/etc/tosblog/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 1

#GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-59931269-1'

with open('/etc/tosblog/tosblog/google_analytics_key.txt') as f:
    GOOGLE_ANALYTICS_PROPERTY_ID = f.read().strip()
	
# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.contenttypes',
	'django_comments',
	'mptt',
	'tagging',
	'django_xmlrpc',
	'zinnia',
	'zinnia_tinymce',
	'sorl.thumbnail',
	'envelope',
	'honeypot',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	#'HoneypotMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)


ZINNIA_SPAM_CHECKER_BACKENDS = (
  'zinnia.spam_checker.backends.mollom',
  'zinnia.spam_checker.backends.all_is_spam',
  'zinnia.spam_checker.backends.automattic',
  'zinnia.spam_checker.backends.long_enough',
  'zinnia.spam_checker.backends.typepad',
)

with open('/etc/tosblog/tosblog/mollom_public_key.txt') as f:
    MOLLOM_PUBLIC_KEY = f.read().strip()
	
with open('/etc/tosblog/tosblog/mollom_private_key.txt') as f:
    MOLLOM_PRIVATE_KEY = f.read().strip()
	
with open('/etc/tosblog/tosblog/akismet_secret_api_key.txt') as f:
    AKISMET_SECRET_API_KEY = f.read().strip()
	
	
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/django/django_project/templates/',
        ],
		'APP_DIRS': True,
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
                'django.contrib.messages.context_processors.messages',
				'django.core.context_processors.request',
            ],
        },
    },
]


ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

with open('/etc/tosblog/tosblog/database.txt') as f:
    DBPASS = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': DBPASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/django/django_project/django_project/static'



EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'webmaster@tosblog.us'
#EMAIL_HOST_PASSWORD = ''
with open('/etc/tosblog/tosblog/emailpass.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip()
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'webmaster@tosblog.us'

with open('/etc/tosblog/honeypot.txt') as f:
    HONEYPOT_FIELD_NAME = f.read().strip()
#HONEYPOT_FIELD_NAME = 