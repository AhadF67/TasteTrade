# Generated by Django 4.2.15 on 2024-08-25 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_category_remove_order_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='expiry_date',
        ),
    ]