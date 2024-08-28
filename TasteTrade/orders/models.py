from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    DURATION_CHOICES_FIRST = [
        ('once_a_week', 'Once a Week'),
        ('twice_a_week', 'Twice a Week'),
    ]

    DURATION_CHOICES_SECOND = [
        ('one_month', 'One Month'),
        ('two_months', 'Two Months'),
        ('three_months', 'Three Months'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('rejected', 'Rejected')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_first = models.CharField(max_length=20, choices=DURATION_CHOICES_FIRST, blank=True, null=True)
    duration_second = models.CharField(max_length=20, choices=DURATION_CHOICES_SECOND, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_number}"

    def save(self, *args, **kwargs):
        # Check if the order is being created or updated
        if self.pk is None:
            # New order, reduce the product quantity
            self.product.quantity -= self.quantity
            self.product.save()
        else:
            # Existing order, check if status is changing
            old_order = Order.objects.get(pk=self.pk)
            if old_order.status in ['approved', 'completed', 'pending'] and self.status in ['canceled', 'rejected']:
                # If order was approved/completed/pending and now is canceled/rejected, add the quantity back
                self.product.quantity += self.quantity
                self.product.save()
        
        super(Order, self).save(*args, **kwargs)

class Review(models.Model):
    order_number = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_number} - {self.supplier_name}"