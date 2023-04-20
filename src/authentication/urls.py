from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthenticationViewSet

router = DefaultRouter()

router.register("authentication", AuthenticationViewSet, basename="authentication")

urlpatterns = [
    path("", include(router.urls)),
]