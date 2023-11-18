from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils.tracker import FieldTracker


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
    comments = models.TextField("Observações", max_length=255, default="")
    status = models.CharField(
        "Status",
        max_length=30,
        choices=Roles.choices,
        default=Roles.HEALTHY,
    )
    tracker = FieldTracker()

    def __str__(self):
        return self.name


class HiveSnapshot(TimeStampedModel):
    changed_by = models.ForeignKey(
        "authentication.User",
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        "Nome",
        max_length=255,
        null=True,
        blank=True,
    )
    comments = models.TextField(
        "Observações",
        max_length=255,
        null=True,
        blank=True,
    )
    status = models.CharField(
        "Status",
        max_length=30,
        choices=Hive.Roles.choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Collection(TimeStampedModel):
    hive = models.ForeignKey(
        "hives.Hive",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    registered_by = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return self.quantity
