from django.urls import path

from .views import (
    CarsView,
    CreateCar,
    GetCarView,
    UpdateCarView,
    DeleteCarView
)

urlpatterns = [
    # cars
    path('cars/', CarsView.as_view()),
    path('create/', CreateCar.as_view()),
    path('car/<int:pk>/', GetCarView.as_view()),
    path('update_car/<int:pk>/', UpdateCarView.as_view()),
    path('delete_car/<int:pk>/', DeleteCarView.as_view()),
]
