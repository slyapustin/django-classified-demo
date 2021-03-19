# -*- coding:utf-8 -*-
import os

import environ

env = environ.Env(
	DEBUG=(bool, True),
	CACHE_URL=(str,  'locmemcache://'),
	EMAIL_URL=('EMAIL_URL', 'smtp://[user]:[password]@[host.domain.tld]:[portnumber]'),
)

DEBUG = env('DEBUG')
SECRET_KEY = ''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('Demo Classified Admin', os.environ.get('ADMIN_EMAIL', 'your@email.add')),
)

MANAGERS = ADMINS

# Expected comma separated string with the ALLOWED_HOSTS list
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,.herokuapp.com').split(',')

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'name',
        #'USER': 'user',
        #'PASSWORD': 'pass',
        #'HOST': '127.0.0.1',
        #'PORT': '3306'
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': env.cache()
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#
# TIME_ZONE = 'Europe/London'
# TIME_ZONE = 'America/Adak'
# TIME_ZONE = 'Africa/Abidjan'
# TIME_ZONE = 'Antarctica/Casey'
# TIME_ZONE = 'Arctic/Longyearbyen'
# TIME_ZONE = 'Atlantic/Reykjavik'
# TIME_ZONE = 'GMT'

TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

# check site id in admin
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
# If using manage.py runserver" the resulting server will not deliver media files 
# unless DEBUG = True.
# media is served locally in this example
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
# media is served locally in this example
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: 'http://foo.com/static/admin/', '/static/admin/'.

# Additional locations of static files
STATICFILES_DIRS = (

    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    os.path.join(BASE_DIR, 'demo/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

#For remote file storage
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


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


ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Django Classified context processors
                'django_classified.context_processors.common_values'
            ],
            'debug': True
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    
    'bootstrapform',
    'bootstrap4',
    'sorl.thumbnail',
    'django_classified',
    'storages',

    'fontawesome_5', # only used on log-in page for social network icons
    
    'demo',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # enable/disable providers as required
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.openid',
	# etc
]

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
PROFILE_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/'

DCF_SITE_NAME = 'Django Classified Demo'

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'your@email.add')

# Configure email Backend via EMAIL_URL
vars().update(env.email_url())
EMAIL_URL=env('EMAIL_URL')


DCF_CURRENCY = 'GBP'
DCF_DISPLAY_EMPTY_GROUPS = True


# DCF_IMAGE_STORAGE
# Assumes that submitted changes have been incorporated into 'Image' model 
# and 'django_classified/settings.py.
#
# default is 'images'
# date string formats are interpreted as at image upload, and can
# be extended eg: 'images/items/%Y/%m/%d/%H/%M/%S'
DCF_IMAGE_STORAGE = 'images/items/%Y/%m/%d'

#GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID')

#AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL')
#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#AWS_QUERYSTRING_AUTH = False
#AWS_DEFAULT_ACL='public-read'

##############################
#allauth settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 #blocked after this number of failed login attempts
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 600 # number of seconds for duration of timeout
ACCOUNT_LOGOUT_REDIRECT_URL ='/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_PRESERVE_USERNAME_CASING = False # reduces the delays in iexact lookups
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_MAX_LENGTH = 20 # custom setting, via 'demo.adapter.CustomProcessAdapter'
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_USERNAME_VALIDATORS = None
ACCOUNT_PASSWORD_MAX_LENGTH = 20 # custom setting, via 'demo.adapter.CustomProcessAdapter'

##############################

#Account adapters
ACCOUNT_ADAPTER = 'demo.adapter.CustomProcessAdapter'

#Account Signup
ACCOUNT_FORMS = {'signup': 'demo.forms.SignupForm',}

# Social network settings
# see: https://django-allauth.readthedocs.io/en/latest/providers.html
# set-up social auth apps in admin
# OpenID does not need an application in admin
SOCIALACCOUNT_PROVIDERS = {
	'twitter': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    },
    'openid': {'SERVERS': [
            dict(id='yahoo',
                 name='Yahoo',
                 openid_url='http://me.yahoo.com'),
            dict(id='hyves',
                 name='Hyves',
                 openid_url='http://hyves.nl'),
            dict(id='google',
                 name='Google',
                 openid_url='https://www.google.com/accounts/o8/id'),
            dict(id='steam',
                name='Steam',
                openid_url='https://steamcommunity.com/openid')
        ]
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
}
SOCIALACCOUNT_QUERY_EMAIL=ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_EMAIL_REQUIRED=ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_STORE_TOKENS=False

BOOTSTRAP4 = {
	#overrides defaults
	'horizontal_label_class': 'col-sm-2 col-lg-2',
	'horizontal_field_class': 'col-sm-10 col-lg-10',
}