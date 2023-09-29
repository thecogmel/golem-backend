from rest_framework import serializers

from authentication.serializers import UserSerializer

from .models import Hive


class HiveSerializer(serializers.ModelSerializer):
    responsible_user = UserSerializer(many=False)

    class Meta:
        model = Hive
        fields = [
            "id",
            "name",
            "description",
            "status",
            "responsible_user",
            "created",
            "modified",
        ]
