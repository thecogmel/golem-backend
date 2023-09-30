from rest_framework import serializers

from authentication.serializers import UserSerializer

from .models import Hive


class HiveSerializer(serializers.ModelSerializer):
    responsible = UserSerializer(many=False, required=False)

    class Meta:
        model = Hive
        fields = [
            "id",
            "name",
            "description",
            "status",
            "responsible",
            "created",
            "modified",
        ]
