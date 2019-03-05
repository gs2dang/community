import requests

from .base import *

DEBUG = False

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

WSGI_APPLICATION = 'config.wsgi.production.application'

ALLOWED_HOSTS = SECRETS['ALLOWED_HOSTS']

DATABASES = SECRETS['DATABASES']

# Health Check 도메인을 허용하는 코드
try:
    EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass

# S3 Storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'ap-northeast-2'
