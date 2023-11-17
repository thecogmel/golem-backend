from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Collection, Hive
from .serializers import CollectionSerializer, HiveSerializer


class HiveViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filterset_fields = ["hive"]
