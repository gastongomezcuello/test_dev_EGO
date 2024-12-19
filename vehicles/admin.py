from django.contrib import admin

from .models import Category, Car


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "price", "category")
    list_filter = ("category", "year", "price")
    search_fields = ("name",)
    ordering = ("-year",)
