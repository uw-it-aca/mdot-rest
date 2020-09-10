from .base_settings import *
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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

# Authentication Groups
ADMIN_AUTHZ_GROUP = os.getenv('MDOT_REST_ADMIN_GROUP', 'u_test_admin')
 