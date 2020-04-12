from domain import DOMAIN_SETTINGS

DOMAIN = DOMAIN_SETTINGS

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# disable default behaviour
RETURN_MEDIA_AS_BASE64_STRING = False

# return media as URL instead
RETURN_MEDIA_AS_URL = True

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Skip this block if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
# MONGO_AUTH_SOURCE = '<dbname>'

MONGO_DBNAME = 'apitest'
API_VERSION = 'v1'
URL_PREFIX = 'api'
## CORS
X_DOMAINS = '*'
X_ALLOW_CREDENTIALS = True
X_HEADERS = ['Authorization','Content-type', 'If-Modified', "If-Match", 'Cache-Control']
EMBEDDING=True
