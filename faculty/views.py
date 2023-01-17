from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .serializer import FacultySerializer
from .models import Faculty


class FacultiesView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class CreateFacultyView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class GetFacultyById(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class UpdateFacultyView(UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DeleteFacultyView(DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
