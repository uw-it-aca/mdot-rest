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

# settings for local development
if DEBUG:
    MOCK_SAML_ATTRIBUTES['isMemberOf'] = ['u_test_admin']
    MEDIA_ROOT = '/app/'
    MEDIA_URL = '/media/'

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME', '')
    GS_PROJECT_ID = os.getenv('STORAGE_PROJECT_ID', '')
    GS_LOCATION = os.path.join(os.getenv('ENV'), 'media')
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        '/gcs/credentials.json'
    )

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

# Authentication Groups
ADMIN_AUTHZ_GROUP = os.getenv('MDOT_REST_ADMIN_GROUP', 'u_test_admin')
 