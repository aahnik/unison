#!/bin/bash

# run tailwindcss in the background
# redirect stdout and stderr to tailwind.logs
npm run dev > tailwind.logs 2>&1 &


# activate the virtual environment
source .venv/bin/activate

# move into django project source directory which contains manage.py
cd src

# do the migrations
python manage.py makemigrations
python manage.py migrate

# run the server
python manage.py runserver
