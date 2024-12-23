# Generated by Django 5.1.4 on 2024-12-19 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('features', models.JSONField(blank=True, default=dict)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='vehicles.category')),
            ],
        ),
    ]
