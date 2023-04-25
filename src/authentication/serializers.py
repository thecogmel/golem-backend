from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user or self.username_field.get_user(
            self.validated_data[self.username_field],
        )
        serializer = UserSerializer(user)
        data["user"] = serializer.data

        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
