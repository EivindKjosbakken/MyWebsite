from django.db import models
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)