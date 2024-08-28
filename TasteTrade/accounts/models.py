from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
    phone_number = models.CharField(max_length=15, blank=True)
    cr_file = models.FileField(upload_to='documents/cr_files/', blank=True, null=True)
    bank_account_file = models.FileField(upload_to='documents/bank_accounts/', blank=True, null=True)
    iban = models.CharField(
        max_length=24,
        validators=[
            RegexValidator(regex=r'^SA\d{22}$', message="IBAN must start with 'SA' followed by 22 digits.")
        ],
        blank=True,
        null=True,
    )
    is_activated = models.BooleanField(default=False)  # Field to track activation status

    def __str__(self):
        return self.name


