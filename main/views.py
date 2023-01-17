from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import Car
from .serializer import CarSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CreateCar(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class GetCarView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UpdateCarView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DeleteCarView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
