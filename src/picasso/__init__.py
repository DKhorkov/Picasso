import os
import shutil

from .celery import app as celery_app

__all__ = ('celery_app',)

os.makedirs('database/', exist_ok=True)  # creating database folder for correct migration work
shutil.rmtree('src/database/', ignore_errors=True)  # deletes empty database folder, created during celery workrer launch
