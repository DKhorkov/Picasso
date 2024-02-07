from rest_framework import viewsets

from .models import File
from .serializers import FileSerializer
from .tasks import process_uploaded_file


class UploadFileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data

        # processing file using celery:
        process_uploaded_file.delay(path_to_file=instance['file'], db_entry_id=instance['id'])
        return response


class ShowFilesView(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
