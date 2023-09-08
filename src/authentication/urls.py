from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LoginViewSet,
    LogoutView,
    ResetPasswordView,
    UpdatePasswordView,
    UserViewSet,
)

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginViewSet.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("update-password/", UpdatePasswordView.as_view(), name="update-password"),
]
