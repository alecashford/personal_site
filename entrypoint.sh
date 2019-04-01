#!/bin/sh
# If the secrets file exists, read it in.
if [ -f secrets.sh ]; then
  . secrets.sh
fi

pipenv run python manage.py runserver 0.0.0.0:8000

# Now run the main container CMD, replacing this script.
exec "$@"