from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .serializer import RegionSerializer
from .models import Region


class RegionsView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CreateRegionView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class GetRegionById(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class UpdateRegionView(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DeleteRegionView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
