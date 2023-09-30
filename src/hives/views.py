from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Hive
from .serializers import HiveSerializer


class HiveViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer
