from .models import Car
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import CarSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CreateCar(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
