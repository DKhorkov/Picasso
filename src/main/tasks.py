from celery import shared_task
from time import sleep

from .models import File
from .configs import FILE_PROCESSING_TIME


@shared_task
def process_uploaded_file(path_to_file: str, db_entry_id: int):
    print(f'Processing file with next path: {path_to_file}...')
    sleep(FILE_PROCESSING_TIME)

    db_entry = File.objects.get(id=db_entry_id)
    db_entry.processed = True
    db_entry.save()
