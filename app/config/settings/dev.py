from .base import *

DEBUG = True


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bulletin_board_dev',
        'USER': 'master',
        'PASSWORD': 'master',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += [
    'django_extensions',
]