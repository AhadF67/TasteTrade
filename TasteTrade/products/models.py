from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_new = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=100)  # Change this if not using Category model
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

