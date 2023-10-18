from .base_settings import *
from google.oauth2 import service_account
import os

if os.getenv('ENV', 'localdev') == 'localdev':
    DEBUG = True
else:
    DEBUG = False

INSTALLED_APPS += (
    'mdot_rest',
    "rest_framework",
    "django_filters",
)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# settings for local development
if os.getenv('AUTH', 'NONE') == 'SAML_MOCK':
    MOCK_SAML_ATTRIBUTES['isMemberOf'] = ['u_test_admin']

if os.getenv('ENV', 'localdev') == 'localdev':
    MEDIA_ROOT = '/app/'
    MEDIA_URL = '/media/'
else:
    STORAGES = {
        'default': {
            'BACKEND': 'storages.backends.gcloud.GoogleCloudStorage',
            'OPTIONS': {
                'project_id': os.getenv('STORAGE_PROJECT_ID', ''),
                'bucket_name': os.getenv('STORAGE_BUCKET_NAME', ''),
                'location': os.path.join(os.getenv('ENV', ''), 'media'),
                'credentials': service_account.Credentials.from_service_account_file(
                    '/gcs/credentials.json'),
            }
        },
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
    }
    CSRF_TRUSTED_ORIGINS = ['https://' + os.getenv('CLUSTER_CNAME')]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

# Authentication Groups
ADMIN_AUTHZ_GROUP = os.getenv('ADMIN_AUTHZ_GROUP', 'u_test_admin')
