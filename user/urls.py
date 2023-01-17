from django.urls import path

from .views import (
    UsersView,
    CreateUserView,
    GetUserById,
    UpdateUserView,
    DeleteUserView
)

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('create_user/', CreateUserView.as_view()),
    path('user/<int:pk>/', GetUserById.as_view()),
    path('update_user/<int:pk>/', UpdateUserView.as_view()),
    path('delete_user/<int:pk>/', DeleteUserView.as_view()),
]
