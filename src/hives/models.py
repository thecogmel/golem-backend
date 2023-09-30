from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Hive(TimeStampedModel):
    class Roles(models.TextChoices):
        HEALTHY = "HEALTHY", _("Healthy")
        DECLINING = "DECLINING", _("Declining")
        DEAD_OR_ABANDONED = "DEAD_OR_ABANDONED", _("Dead or Abandoned")

    responsible = models.ForeignKey(
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
