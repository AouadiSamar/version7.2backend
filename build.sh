#!/bin/bash

# Installer les dépendances
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Appliquer les migrations de base de données
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
