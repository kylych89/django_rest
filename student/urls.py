from django.urls import path

from .views import (
    StudentsView,
    CreateStudentView,
    GetStudentById,
    UpdateStudentView,
    DeleteStudentView
)

urlpatterns = [
    path('students/', StudentsView.as_view()),
    path('create_student/', CreateStudentView.as_view()),
    path('student/<int:pk>/', GetStudentById.as_view()),
    path('update_student/<int:pk>/', UpdateStudentView.as_view()),
    path('delete_student/<int:pk>/', DeleteStudentView.as_view()),
]
