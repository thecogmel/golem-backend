from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, LoginViewSet

router = DefaultRouter()

router.register("authentication", UserViewSet, basename="authentication")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginViewSet.as_view(), name="login"),

]