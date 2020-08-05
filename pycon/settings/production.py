import os

from .defaults import *

from google.oauth2 import service_account

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.rq import RqIntegration
from sentry_sdk.integrations.redis import RedisIntegration

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '*'
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    '',
]

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

CSP_DEFAULT_SRC = ("'none'", )
CSP_STYLE_SRC = ("'self'", "https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css")
CSP_SCRIPT_SRC = ("'self'", )
CSP_IMG_SRC = ("'self'", )
CSP_FONT_SRC = ("'self'", )
CSP_BASE_URI = ("'self'", )
CSP_FRAME_ANCESTORS = ("'self'", )
CSP_FRAME_SRC = ("'self'", )
CSP_FORM_ACTION = ("'self'", )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST' : os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'CONN_MAX_AGE' : 60
        # 'OPTIONS': {
        #     'sslmode': 'verify-ca',
        #     'sslrootcert': 'server-ca.pem',
        #     'sslkey': 'client-key.pem',
        #     'sslcert': 'client-cert.pem'
        # }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URL'),
        'OPTIONS': {
            'DEFAULT_TIMEOUT': 10,
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
    },
}

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default'
    },
    'low': {
        'USE_REDIS_CACHE': 'default'
    },
    'high': {
        'USE_REDIS_CACHE': 'default'
    }
}

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
            ]
        },
    },
]

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware'
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "default"

FILE_UPLOAD_MAX_MEMORY_SIZE = 10000000

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file('travis_sak.json')

GS_CACHE_CONTROL = 'max-age=86400'

GS_BUCKET_NAME = "pycon-demo"

GS_DEFAULT_ACL = "publicRead"

STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

EMAIL_HOST = 'mail.host.com'

EMAIL_HOST_USER = 'hi@email.com'

EMAIL_HOST_PASSWORD = "password_goes_here"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_REPLY_TO = "hi@email.com"

sentry_sdk.init(
    dsn="https://45aea208c5f14ce0a2b6ee1313adc91a@o283136.ingest.sentry.io/5378914",
    release="PyconAfrica2020",
    integrations=[DjangoIntegration(), RqIntegration(), RedisIntegration()]
)