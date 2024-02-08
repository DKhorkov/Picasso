#!/bin/bash


until cd /app/src
do
    echo "Waiting for server volume..."
done

celery -A picasso worker -l info