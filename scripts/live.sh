#!/bin/bash

# run tailwindcss in the background
npm run dev &

# activate the virtual environment
source .venv/bin/activate

# move into django project source directory which contains manage.py
cd src

# do the migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic -c --no-input

# run the server
python manage.py runserver
