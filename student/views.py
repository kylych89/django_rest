from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .serializer import StudentSerializer
from .models import Student


class StudentsView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetStudentById(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
