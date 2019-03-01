from .base import *

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'base.json')))

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.production.application'

ALLOWED_HOSTS = SECRETS['ALLOWED_HOSTS']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = SECRETS['DATABASES']