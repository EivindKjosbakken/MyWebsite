from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='./images')
    class Meta:
        db_table = "myapp_image"