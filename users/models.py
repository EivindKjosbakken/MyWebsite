from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=120) # max_length = required
    age         = models.DecimalField(decimal_places=2, max_digits=10000)
    gender       = models.CharField(max_length=10)
    description     = models.CharField(max_length=150)
    


