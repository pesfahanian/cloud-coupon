from decouple import config, Csv

from .base import *  # noqa

DEBUG = False

# * ------------------------------- API --------------------------------
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='*',
    cast=Csv(),
)

CORS_ORIGIN_ALLOW_ALL = config(
    'CORS_ORIGIN_ALLOW_ALL',
    default=True,
    cast=bool,
)

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://0.0.0.0:8800',
    cast=Csv(),
)

CSRF_COOKIE_SECURE = config(
    'CSRF_COOKIE_SECURE',
    default=False,
    cast=bool,
)
# * --------------------------------------------------------------------
