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

    """ def update(self, instance, validated_data):
        old_instance = instance
        instance = super().update(instance, validated_data)
        updated_fields = instance.tracker.changed()
        old_fields = {}
        for field in updated_fields:
            old_fields[field] = getattr(old_instance, field)
        HiveSnapshot.objects.create(
            changed_by=self.context["request"].user,
            **old_fields,
        ) """


class CollectionSerializer(serializers.ModelSerializer):
    registered_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )  # pegar o user atual
    registered_by_info = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = [
            "id",
            "quantity",
            "hive",
            "registered_by",
            "registered_by_info",
            "created",
            "modified",
        ]

    # Ao criar solicita apenas o ID do usuário, mas ao retornar o objeto completo
    # def to_representation(self, instance):
    #    data = super().to_representation(instance)
    #    if instance.registered_by is not None:
    #       data["registered_by"] = UserSerializer(instance.registered_by).data
    #   return data

    def get_registered_by_info(self, obj):
        return UserSerializer(obj.registered_by).data
