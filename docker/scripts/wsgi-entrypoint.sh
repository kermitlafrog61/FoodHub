#!/bin/sh

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput --first_name=Admin --last_name=Admin

python manage.py runserver 0.0.0.0:8000
