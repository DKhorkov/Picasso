FROM python:3
LABEL authors="dkhorkov"

WORKDIR /app

COPY . /app

# Changing permissions for correct work inside docker:
RUN chmod +x /app/docker/celery_entrypoint.sh
RUN chmod +x /app/docker/django_entrypoint.sh

# Installing python requirements:
RUN pip install -r requirements.txt
