from django.db import models
from django.contrib.auth.models import User 
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)


    def str(self):
        return self.name