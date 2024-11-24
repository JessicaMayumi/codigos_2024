from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=255, default="Product")
    description = models.TextField(default="Description of Product ")
    price       = models.TextField(default="19.99")
    summary     = models.TextField(default="this is cool!")