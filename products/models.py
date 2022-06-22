from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    reviews     = models.CharField(max_length=150)
    featured    = models.BooleanField(default=False) # null=True, default=True

    #easier if we change somethingh
    def get_absolute_url(self):
        return reverse("products:productDetail", kwargs={"id": self.id})                  #f"/products/{self.id}/"