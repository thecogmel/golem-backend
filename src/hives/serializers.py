from rest_framework import serializers

from authentication.serializers import UserSerializer

from .models import Hive


class HiveSerializer(serializers.ModelSerializer):
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

    # Ao criar solicita apenas o ID do usuário, mas ao retornar o objeto completo
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.responsible is not None:
            data["responsible"] = UserSerializer(instance.responsible).data
        return data
