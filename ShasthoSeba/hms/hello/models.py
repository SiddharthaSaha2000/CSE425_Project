from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default='')
    hospital = models.CharField(max_length=255, default='')

    def _str_(self):
        return self.title