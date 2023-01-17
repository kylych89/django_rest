from django.urls import path

from .views import (
    RegionsView,
    CreateRegionView,
    GetRegionById,
    UpdateRegionView,
    DeleteRegionView
)

urlpatterns = [
    path('regions/', RegionsView.as_view()),
    path('create_region/', CreateRegionView.as_view()),
    path('region/<int:pk>/', GetRegionById.as_view()),
    path('update_region/<int:pk>/', UpdateRegionView.as_view()),
    path('delete_region/<int:pk>/', DeleteRegionView.as_view()),
]
