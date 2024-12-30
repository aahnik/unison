#!/bin/bash

# you may be required to use python3 instead of python in some systems

# Apply database migrations
python src/manage.py migrate

# Create superuser if needed
python src/manage.py ensure_superuser

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 --keep-alive 5 --max-requests 1000 --chdir src temple_web.wsgi:application
