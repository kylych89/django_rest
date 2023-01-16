from .models import Car
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializer import CarSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CreateCar(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
