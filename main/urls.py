from django.urls import path
from .views import CarsView, CreateCar, UpdateDeleteCarView

urlpatterns = [
    path('cars/', CarsView.as_view()),
    path('create/', CreateCar.as_view()),
    path('update/<int:pk>/', UpdateDeleteCarView.as_view()),
    path('delete/<int:pk>/', UpdateDeleteCarView.as_view()),
]
