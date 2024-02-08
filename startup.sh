#!/bin/bash

# installing python requirements:
pip install -r requirements.txt

# updating system, installing redis nad launching redis server:
sudo docker run -d -p 6379:6379 redis

# alternative to redis in docker:
#sudo apt update
#sudo apt install redis
#gnome-terminal -- redis-server -h redis


# launching celery worker:
gnome-terminal -- python -m celery --workdir src -A picasso worker -l info

# configuring and launching django:
python src/manage.py migrate
python src/manage.py makemigrations main
python src/manage.py migrate
python src/manage.py runserver
