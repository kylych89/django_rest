from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Area
from .serializer import AreaSerializer


class AreasView(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class CreateAreaView(CreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class GetAreaById(RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class UpdateAreaView(UpdateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class DeleteAreaView(DestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
