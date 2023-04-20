from rest_framework import viewsets

from .models import User
from .serializers import AuthenticationSerializer


class AuthenticationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthenticationSerializer