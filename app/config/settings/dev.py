from .base import *

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'base.json')))

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS = SECRETS['ALLOWED_HOSTS']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = SECRETS['DATABASES']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    'django_extensions',
]