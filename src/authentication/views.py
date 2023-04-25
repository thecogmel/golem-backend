import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User
from .serializers import LoginSerializer, LogoutSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = User
        fields = "__all__"


class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "tokens": {
                    "access": serializer.validated_data["access"],
                    "refresh": serializer.validated_data["refresh"],
                },
                "user": serializer.validated_data["user"],
            },
            status=status.HTTP_200_OK,
        )


class RefreshTokenView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get_user_from_jwt_raw_token(self) -> User:
        token = jwt.decode(
            self,
            settings.SECRET_KEY,
            algorithms=settings.SIMPLE_JWT["ALGORITHM"],
        )
        return get_object_or_404(User, id=token["user_id"])

    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError:
            return Response(
                {"detail": ("Invalid token.")},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = self.get_user_from_jwt_raw_token(request.data["refresh"])
        user_data = self.get_serializer(user=user).data

        return Response(
            {"user": user_data, "tokens": serializer.validated_data},
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    def post(self, request):
        try:
            serializer = LogoutSerializer(data=request.data["refresh"])
            serializer.is_valid(raise_exception=True)

            RefreshToken(serializer.validated_data["refresh"]).blacklist()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
