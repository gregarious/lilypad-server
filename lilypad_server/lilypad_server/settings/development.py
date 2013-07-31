import os

from lilypad_server.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if os.environ.get('CLIENT_APP_PARENT') is None:
    raise ImproperlyConfigured('Must define environment variable named CLIENT_APP_PARENT')

STATICFILES_DIRS = (
    os.environ.get('CLIENT_APP_PARENT'),
)

# should be irrelevant for DEBUG mode, but Django is getting mad
# at our redirect setup if it's left blank. just use default tmp dir
import tempfile
STATIC_ROOT = tempfile.gettempdir()
