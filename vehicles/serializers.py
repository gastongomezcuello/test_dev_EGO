from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "description",
            "image_url",
            "year",
            "price",
            "features",
            "category",
            "category_name",
        )
