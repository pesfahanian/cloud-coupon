from datetime import timedelta
from pathlib import Path

from decouple import config

from config.logger import Filter as _Filter, get_logging

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config(
    'SECRET_KEY',
    default=  # noqa
    r'django-insecure-6ognx_g8i3=x-7op@d$x@26qh_n*308#t&s5zy&!fs526+m3rs',
)

INSTALLED_APPS = [
    # * Apps
    'apps.core.apps.CoreConfig',
    'apps.user.apps.UserConfig',
    'apps.wallet.apps.WalletConfig',

    # * Packages
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',

    # * Healthcheck
    'health_check',
    'health_check.db',
    'health_check.contrib.migrations',

    # * Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # * Packages
    'corsheaders.middleware.CorsMiddleware',

    # * Default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

DATETIME_INPUT_FORMAT = '%Y-%m-%d %H:%M:%S'

DATE_FORMAT = '%Y-%m-%d'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


class Filter(_Filter):
    service = 'couponing'


LOGGING = get_logging(filter=Filter)

AUTH_USER_MODEL = 'user.User'

ADMIN_USERNAME = config(
    'ADMIN_USERNAME',
    default='admin',
)
ADMIN_PASSWORD = config(
    'ADMIN_PASSWORD',
    default='admin',
)

# * ----------------------------- Postgres -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config(
            'DB_NAME',
            default='an-couponing',
        ),
        'USER': config(
            'DB_USER',
            default='postgres',
        ),
        'PASSWORD': config(
            'DB_PASSWORD',
            default='1234',
        ),
        'HOST': config(
            'DB_HOST',
            default='0.0.0.0',
        ),
        'PORT': config(
            'DB_PORT',
            default=5432,
            cast=int,
        ),
    }
}
# * --------------------------------------------------------------------

# * ------------------------------- API --------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

PUBLIC_KEY_PATH = f'{BASE_DIR}/keys/jwtRS256.key.pub'

PRIVATE_KEY_PATH = f'{BASE_DIR}/keys/jwtRS256.key'

PAGE_SIZE = config(
    'PAGE_SIZE',
    default=10,
    cast=int,
)

ACCESS_TOKEN_LIFETIME = config(
    'ACCESS_TOKEN_LIFETIME',
    default=1440,
    cast=int,
)

REFRESH_TOKEN_LIFETIME = config(
    'REFRESH_TOKEN_LIFETIME',
    default=16,
    cast=int,
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(REFRESH_TOKEN_LIFETIME),
    'SIGNING_KEY': open(PRIVATE_KEY_PATH).read(),
    'VERIFYING_KEY': open(PUBLIC_KEY_PATH).read(),
    'ALGORITHM': 'RS256',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTTokenUserAuthentication', ),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':
    PAGE_SIZE,
    'DATETIME_FORMAT':
    DATETIME_FORMAT,
    'DATE_FORMAT':
    DATE_FORMAT,
}
# * --------------------------------------------------------------------
