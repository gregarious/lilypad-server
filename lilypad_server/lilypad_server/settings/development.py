from lilypad_server.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'sandbox'
    }
}
