from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    year = models.IntegerField(validators=[MaxValueValidator(datetime.now().year)])
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    features = models.JSONField(blank=True, default=dict)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    def __str__(self):
        return self.name
