# Generated by Django 5.1.4 on 2024-12-19 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2024)]),
        ),
    ]
