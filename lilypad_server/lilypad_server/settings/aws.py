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

STATIC_ROOT = os.path.join(
				os.path.dirname(		# <ROOT>
					os.path.dirname(		# lilypad_server/
						os.path.dirname(		# lilypad_server/
							os.path.dirname(		# settings/
								os.path.abspath(__file__))))), 
				'static')

# STATIC_URL setting doesn't appear to do anything with AWS. Let's at least be explicit about it.
STATIC_URL = '/static/'