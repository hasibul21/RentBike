# Generated by Django 4.0.2 on 2022-02-28 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_bikepost_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)]),
        ),
    ]
