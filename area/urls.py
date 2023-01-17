from django.urls import path

from .views import (
    AreasView,
    CreateAreaView,
    GetAreaById,
    UpdateAreaView,
    DeleteAreaView
)

urlpatterns = [
    path('areas/', AreasView.as_view()),
    path('create_area/', CreateAreaView.as_view()),
    path('area/<int:pk>/', GetAreaById.as_view()),
    path('update_area/<int:pk>/', UpdateAreaView.as_view()),
    path('delete_area/<int:pk>/', DeleteAreaView.as_view()),
]
