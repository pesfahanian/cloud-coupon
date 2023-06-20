#!/bin/bash

set -e

echo "============= Applying Database Migrations ============="
python manage.py migrate

echo "=================== Running Commands ==================="
python manage.py createadmin
python manage.py seed

echo "=================== Starting Servers ==================="
gunicorn -c config/gunicorn.py config.wsgi
# python manage.py runserver 0.0.0.0:8800
