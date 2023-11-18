from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response

from .models import Collection, Hive
from .serializers import CollectionSerializer, HiveSerializer


class HiveViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer

    @action(detail=True, methods=["get"])
    def metrics(self, request, pk=None):
        hive = self.get_object()
        collection_average = Collection.objects.filter(hive=hive).aggregate(
            collection_average=models.Avg("quantity"),
        )

        return Response(collection_average)


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filterset_fields = {"hive": ["exact"], "created": ["gte", "lte"]}

    @action(detail=False, methods=["get"])
    def metrics(self, request, pk=None):
        collection_average = Collection.objects.aggregate(
            collection_average=models.Avg("quantity"),
        )

        return Response(collection_average)
