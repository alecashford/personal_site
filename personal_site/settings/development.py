from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DEV_DB_NAME"),
        "USER": os.environ.get("APP_DB_USERNAME"),
        "PASSWORD": os.environ.get("APP_DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

HEAP_ENV_ID = "3464552814"
