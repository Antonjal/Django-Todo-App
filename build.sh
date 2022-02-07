#!/usr/bin/env bash
# exit on error
set -o errexit

pip install

python manage.py migrate