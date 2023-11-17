from rest_framework import serializers

from authentication.serializers import UserSerializer

from .models import Collection, Hive


class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = [
            "id",
            "name",
            "comments",
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


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "quantity",
            "hive",
            "registered_by",
            "created",
            "modified",
        ]

    # Ao criar solicita apenas o ID do usuário, mas ao retornar o objeto completo
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.registered_by is not None:
            data["registered_by"] = UserSerializer(instance.registered_by).data
        return data
