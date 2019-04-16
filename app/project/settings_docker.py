from project.settings import *

if os.environ.get('DJANGO_EMAIL_HOST'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.environ['DJANGO_EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['DJANGO_EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_HOST_PASSWORD']
    EMAIL_PORT = os.environ['DJANGO_EMAIL_PORT']
    EMAIL_USE_SSL = os.environ['DJANGO_EMAIL_USE_SSL'] == 'True'
    EMAIL_USE_TLS = os.environ['DJANGO_EMAIL_USE_TLS'] == 'True'
    EMAIL_FROM = os.environ['DJANGO_EMAIL_FROM']

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID')
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
GOOGLE_SITE_VERIFICATION_ID = os.environ.get('GOOGLE_SITE_VERIFICATION_ID')
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_APP_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

# Fixed proxy SSL header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
