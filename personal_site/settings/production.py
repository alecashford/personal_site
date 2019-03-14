from .base import *

DEBUG = False
ALLOWED_HOSTS = ["www.alecashford.com", "ashford.sh"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PROD_DB_NAME"),
        "USER": os.environ.get("APP_DB_USERNAME"),
        "PASSWORD": os.environ.get("APP_DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

HEAP_ENV_ID = "1936440746"
