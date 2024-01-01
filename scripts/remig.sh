#!/bin/bash

# ==========================================
# THIS IS DANGEROUS AND CAN BREAK PRODUCTION
# ==========================================

# exit


# remigrate

# delete all existing migrations


cd src

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

rm db.sqlite3

# recreate initial migrations
printf "\n\n \033[1;31m Warning!!! update the script to run migrations for all apps\033[0m\n \n\n"
sleep 2
python manage.py makemigrations users
python manage.py makemigrations home
python manage.py makemigrations courses
python manage.py makemigrations donations
python manage.py makemigrations activities


python manage.py migrate

# create superuser
printf "\n\n \033[1;31m CREATE SUPER USER\033[0m\n \n\n"
python manage.py createsuperuser
