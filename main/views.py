from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView)

from .models import Car
from .serializer import CarSerializer, UserSerializer


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
