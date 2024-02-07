from django.db import models


class File(models.Model):
    file = models.FileField(verbose_name='file', upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(verbose_name='uploaded at', auto_now_add=True)
    processed = models.BooleanField(verbose_name='processed', default=False)

    class Meta:
        db_table = 'uploaded_files'
        ordering = ['uploaded_at']

    def __str__(self):
        return self.file.name
