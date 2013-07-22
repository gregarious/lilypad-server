import os

from lilypad_server.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if os.environ.get('CLIENT_APP_PARENT') is None:
    raise ImproperlyConfigured('Must define environment variable named CLIENT_APP_PARENT')

STATICFILES_DIRS = (
    os.environ.get('CLIENT_APP_PARENT'),
)
