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
    image = models.ImageField(upload_to='products/')
    is_new = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_order_set')
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    expiry_date = models.DateField()
    description = models.TextField(blank=True, null=True) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order #{self.id} by {self.user.username}'