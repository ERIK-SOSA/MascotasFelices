#!/bin/bash

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecutar servidor Django
python manage.py runserver 0.0.0.0:8000