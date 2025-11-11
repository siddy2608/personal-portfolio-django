#!/bin/bash
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Checking if database needs initial data..."
# Check if Profile table exists and has data, populate if empty
python << EOF
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_django.settings_production')
django.setup()

from core.models import Profile

if Profile.objects.count() == 0:
    print('Database is empty. Populating with initial data...')
    from django.core.management import call_command
    try:
        call_command('populate_fresher_data')
        print('Successfully populated database with initial data!')
    except Exception as e:
        print(f'Warning: Failed to populate data: {e}')
        print('You can run "python manage.py populate_fresher_data" manually.')
else:
    print('Database already has data. Skipping population.')
EOF

echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 portfolio_django.wsgi:application

