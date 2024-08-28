# Generated by Django 5.0.6 on 2024-08-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('completed', 'Completed'), ('canceled', 'Canceled'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]