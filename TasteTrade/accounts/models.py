from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('sup', 'Supplier'),
        ('bus', 'Business Owner'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name
