#!/bin/bash

# installing python requirements:
pip install -r requirements.txt

# updating system, installing redis nad launching redis server:
#sudo apt update
#sudo apt install redis
#gnome-terminal -- redis-server -h redis
sudo docker run -d -p 6379:6379 redis

# launching celery worker:
gnome-terminal -- python -m celery --workdir src -A picasso worker -l info

# configuring and launching django:
python src/manage.py migrate
python src/manage.py makemigrations main
python src/manage.py migrate
python src/manage.py runserver
