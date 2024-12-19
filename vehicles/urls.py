from django.urls import path
from .views import CarListView, CarByCategoryView, CarDetailView

urlpatterns = [
    path("api/cars/", CarListView.as_view(), name="car-list"),
    path(
        "api/cars/category/<int:category_id>/",
        CarByCategoryView.as_view(),
        name="car-by-category",
    ),
    path("api/cars/<int:car_id>/", CarDetailView.as_view(), name="car-detail"),
]
