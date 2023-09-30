from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HiveViewSet

router = DefaultRouter()

router.register("hives", HiveViewSet, basename="hives")

urlpatterns = [
    path("", include(router.urls)),
]
