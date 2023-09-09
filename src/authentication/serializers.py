from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "name",
            "is_active",
            "is_staff",
            "is_superuser",
            "role",
            "office",
            "sector",
            "password",
        ]


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


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)


class UpdatePasswordSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)
