#!/bin/sh

set -e

echo "Applying all remaining migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting Gunicorn server..."
exec gunicorn Almog1.wsgi:application --bind 0.0.0.0:8000 --workers 3
