#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install dj-database-url
pip install psycopg2

python manage.py migrate
