from .base import *

DEBUG = config('DEBUG', cast=bool, default=True)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())
STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT')

MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT')

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
CORS_ORIGIN_WHITELIST = config("CORS_ORIGIN_WHITELIST", default="http://localhost:3000", cast=Csv())
