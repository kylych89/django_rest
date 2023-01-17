from django.urls import path

from .views import (
    FacultiesView,
    CreateFacultyView,
    GetFacultyById,
    UpdateFacultyView,
    DeleteFacultyView
)

urlpatterns = [
    path('faculties/', FacultiesView.as_view()),
    path('create_faculty/', CreateFacultyView.as_view()),
    path('faculty/<int:pk>/', GetFacultyById.as_view()),
    path('update_faculty/<int:pk>/', UpdateFacultyView.as_view()),
    path('delete_faculty/<int:pk>/', DeleteFacultyView.as_view()),
]
