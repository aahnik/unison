#!/bin/bash

# run tailwindcss in the background
npm run dev &

# activate the virtual environment
source .venv/bin/activate

# move into django project source directory which contains manage.py
cd temple-web

# do the migrations
python manage.py makemigrations
python manage.py migrate

# run the server
python manage.py runserver
