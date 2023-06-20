from .base import *  # noqa

DEBUG = True

INSTALLED_APPS += [
    # * Packages
    'django_extensions',
    'drf_yasg',
]

# * ------------------------------- API --------------------------------
ALLOWED_HOSTS = [
    '*',
]

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    'http://0.0.0.0:8800',
]

CSRF_COOKIE_SECURE = False
# * --------------------------------------------------------------------
