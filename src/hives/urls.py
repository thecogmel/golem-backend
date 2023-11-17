from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CollectionViewSet, HiveViewSet

router = DefaultRouter()

router.register("hives", HiveViewSet, basename="hives")
router.register("collections", CollectionViewSet, basename="collections")

urlpatterns = [
    path("", include(router.urls)),
]
