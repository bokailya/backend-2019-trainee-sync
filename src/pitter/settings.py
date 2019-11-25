import os
from datetime import timedelta
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'cru)q9q-!=#ip!)(i=rawgbjdfxiyrm+znk05iz=5p*w7r9(yh'

DEBUG: bool = bool(int(os.getenv('DEBUG', 1)))  # pylint: disable=invalid-envvar-default

ALLOWED_HOSTS: List[str] = ['*']  # On develop only

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'pitter',
    'api_client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pitter.middleware.ErrorHandlerMiddleware',
]

ROOT_URLCONF = 'pitter.urls'

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
    }
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE', 'postgres'),
        'USER': os.getenv('PGUSER', 'postgres'),
        'PASSWORD': os.getenv('PGPASSWORD', 'postgres'),
        'HOST': os.getenv('PGHOST', 'localhost'),
        'PORT': os.getenv('PGPORT', '5432'),
    }
}

WSGI_APPLICATION = 'pitter.wsgi.application'
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = '/static/'

STATIC_ROOT = '/static'

# DRF

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'EXCEPTION_HANDLER': 'pitter.middleware.custom_exception_handler',
}

# Swagger

SWAGGER_SETTINGS = {
    'DEEP_LINKING': True,
    'SECURITY_DEFINITIONS': {
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'},
        'X-Device-Info': {'type': 'apiKey', 'name': 'X-Device-Info', 'in': 'header'},
    },
}

ASYNCHRONOUS_SERVICE_URL = 'http://pitter_async:8118/api/pitter/v1/recognize'

JSON_WEB_TOKEN_LIFETIME = timedelta(hours=1)

JSON_WEB_TOKEN_PRIVATE_KEY = b'''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
'''

JSON_WEB_TOKEN_PUBLIC_KEY = b'''ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC5RDDq+jfea1hfdqBokQ0nhkaHQ9Opm91HprTNWcar7VHzpL3\
FrYYGZSn68JGtH3hMUYwNkdArfBHmWY4VhebU7zj0Tn/p+vncDmhfXVNJS2cVnp1T17dKQfnf16Xt5jC/EVSX6VX5mbTNIpHqZcwdOE/zj/WBL4+XiWlAQI\
luAmxFfU/nR60XRpsn8RXaHv8zn4Nl5ViSXyV3sTukoAvZd0RMuweumzX2b1l6EObRWEXR+LqjrcDNDh2jNe+jruzwpwd/PvJu7oJNlhamVYvdpkdn1QUns\
Vyf8ukoOfivsanSczdY+Yg2zxzGlXV7AiES21mgmE87Q/VzluMMudKT3SCzunOUYYUSSOIMpCgciXp/RTiMfSnQFaeTuzIW0AmgLW6YY/Pv8uqiPuXLllLB\
WxeWFkC8SfB+36fFumcBMgWqTyC+FSR+pDyaOlBd43YVkE5DAXDWoyvsnGzaDq5VahU5LlXPfRc+e73g5Yb+f9maZNzKssTaxEgZPtkAwls= bokailya@l\
aptop'''
