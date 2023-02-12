from .base import *
from .. import settings

DEBUG = True

SECRET_KEY = 'django-insecure-35g%4bsfth-k#04&ef_3dc1t-0#^@y2jz4#5@!az&fjyf!7ed^'
ALLOWED_HOSTS = ['sh1mu7.privateyebd.com','127.0.0.1']

STATIC_URL = '/static/'
STATIC_ROOT = '/home/sh1mu7/projects/portfolio/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/sh1mu7/projects/portfolio/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ffyjoudx',
        'USER': 'ffyjoudx',
        'PASSWORD': 'kgwGtGcJS6cnUUNwsBAKITvOvH1sopr-',
        'HOST': 'trumpet.db.elephantsql.com',
        'PORT': '5432',
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
