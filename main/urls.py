from django.urls import path
from .views import CarsView, CreateCar

urlpatterns = [
    path('cars/', CarsView.as_view()),
    path('create_car/', CreateCar.as_view()),
]