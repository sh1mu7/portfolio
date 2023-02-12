

from .base import *

DEBUG = config('DEBUG', cast=bool, default=False)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
STATIC_URL = '/static/'
STATIC_ROOT = '/home/sh1mu7/projects/portfolio/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/sh1mu7/projects/portfolio/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
        'ATOMIC_REQUESTS': True,
    }
}
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
