#Bungalow API Setup

virtualenv env
source env/bin/activate

pip install Django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

cd bungalow
chmod 755 manage.py

./manage.py makemigrations
./manage.py migrate

#Load Data
./manage.py import_file {csv_file}

#Start server
./manage.py runserver

#View API
http://127.0.0.1:8000
