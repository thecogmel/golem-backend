from django.db import models
from model_utils.models import TimeStampedModel


class Hive(TimeStampedModel):
    class Roles(models.TextChoices):
        HEALTHY = "HEALTHY", "Saudável"
        DECLINING = "DECLINING", "Declínio"
        DEAD_OR_ABANDONED = "DEAD_OR_ABANDONED", "Morta ou abandonada"

    responsible_user = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", max_length=255)
    status = models.CharField(
        "Status",
        max_length=30,
        choices=Roles.choices,
        default=Roles.HEALTHY,
    )

    def __str__(self):
        return self.name
