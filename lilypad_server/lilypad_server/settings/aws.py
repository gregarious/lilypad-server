import os

os.environ['DATABASE_URL'] = "mysql://%s:%s@%s:%s/%s" % (
	os.environ['RDS_USERNAME'],
	os.environ['RDS_PASSWORD'],
	os.environ['RDS_HOSTNAME'],
	str(os.environ['RDS_PORT']),
	os.environ['RDS_DB_NAME']
)

from lilypad_server.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# The next two settings should match the key/value pair set in 
# `lilypad-server.config` for the namespace 
# `aws:elasticbeanstalk:container:python:staticfiles`

# Should be the path matching the `option_name`
STATIC_URL = '/static/'

# Should be the directory matching the `value` setting
STATIC_ROOT = os.path.join(
				os.path.dirname(		# <ROOT>
					os.path.dirname(		# lilypad_server/
						os.path.dirname(		# lilypad_server/
							os.path.dirname(		# settings/
								os.path.abspath(__file__))))), 
				'static')
