from .base import *
from .. import settings

DEBUG = True

SECRET_KEY = 'django-insecure-35g%4bsfth-k#04&ef_3dc1t-0#^@y2jz4#5@!az&fjyf!7ed^'
ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
