from django.db import models

# Create your models here.


class FamilyMember(models.Model):
    name = models.CharField(max_length=120)
    age = models.DecimalField(decimal_places=0 ,max_digits=3)
    description = models.TextField(max_length=1000)
    #picture = models.ImageField()