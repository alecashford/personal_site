from .base import *

# Be sure to set environment variable "DEPLOYMENT_ENVIRONMENT" to "production"
# in the production server OS

if DEPLOYMENT_ENVIRONMENT == "production":
    from .production import *
else:
    from .development import *
