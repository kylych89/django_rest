from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django.contrib.auth.models import User


from .serializer import UserSerializer


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserById(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
