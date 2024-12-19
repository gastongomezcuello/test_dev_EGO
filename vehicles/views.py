from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from .serializers import CarSerializer


class CarListView(APIView):
    def get(self, request):
        cars = Car.objects.all()

        order_by = request.query_params.get("order_by", "year")
        if order_by not in ["year", "price"]:
            return Response(
                {
                    "error": f"Invalid 'order_by' value. Allowed values are: 'year', 'price'"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_type = request.query_params.get("order_type", "asc")
        if order_type not in ["asc", "desc"]:
            return Response(
                {
                    "error": f"Invalid 'order_type' value. Allowed values are: 'asc', 'desc'"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if order_type == "desc":
            cars = cars.order_by(f"-{order_by}")
        else:
            cars = cars.order_by(order_by)

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarByCategoryView(APIView):
    def get(self, request, category_id):
        cars = Car.objects.filter(category_id=category_id)

        if not cars:
            return Response(
                {"error": "No cars found for the given category"},
                status=status.HTTP_404_NOT_FOUND,
            )

        order_by = request.query_params.get("order_by", "year")
        if order_by not in ["year", "price"]:
            return Response(
                {
                    "error": f"Invalid 'order_by' value. Allowed values are: 'year', 'price'"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_type = request.query_params.get("order_type", "asc")
        if order_type not in ["asc", "desc"]:
            return Response(
                {
                    "error": f"Invalid 'order_type' value. Allowed values are: 'asc', 'desc'"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if order_type == "desc":
            cars = cars.order_by(f"-{order_by}")
        else:
            cars = cars.order_by(order_by)

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class CarDetailView(APIView):
    def get(self, request, car_id):

        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response(
                {"error": "Car not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CarSerializer(car)
        return Response(serializer.data)
