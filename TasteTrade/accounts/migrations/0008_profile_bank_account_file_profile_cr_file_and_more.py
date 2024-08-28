# Generated by Django 5.0.6 on 2024-08-28 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bank_account_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/bank_accounts/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cr_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/cr_files/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='iban',
            field=models.CharField(blank=True, max_length=24, null=True, validators=[django.core.validators.RegexValidator(message="IBAN must start with 'SA' followed by 22 digits.", regex='^SA\\d{22}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]