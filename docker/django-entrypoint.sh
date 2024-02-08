#!/bin/sh

until cd /app/src
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready for migrate..."
    sleep 2
done

until python manage.py makemigrations main
do
    echo "Waiting for db to be ready for makemigrations main..."
    sleep 2
done


until python manage.py migrate
do
    echo "Waiting for db to be ready for migrate..."
    sleep 2
done

python manage.py runserver 0.0.0.0:8000 --noreload
