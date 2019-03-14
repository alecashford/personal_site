from .base import *

# Be sure to set environment variable "STAGE" to "production"
# in the production server OS

if os.environ.get("DEPLOYMENT_ENVIRONMENT") == "production":
    from .production import *
else:
    from .development import *
