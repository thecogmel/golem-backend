from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils.tracker import FieldTracker
from simple_history.models import HistoricalRecords


class Hive(TimeStampedModel):
    class Status(models.TextChoices):
        CAPTURE = "CAPTURE", _("Capture")
        DEVELOPMENT = "DEVELOPMENT", _("Development")
        PRODUCTIVE = "PRODUCTIVE", _("Productive")
        EMPTY_BOX = "EMPTY_BOX", _("Empty Box")

    class SimpleStatus(models.TextChoices):
        REGULAR = "REGULAR", _("REGULAR")
        GOOD = "GOOD", _("GOOD")
        WEAK = "WEAK", _("WEAK")

    name = models.CharField("Nome", max_length=255)
    status = models.CharField(
        "Status",
        max_length=30,
        choices=Status.choices,
        default=Status.CAPTURE,
    )
    queen_status = models.CharField(
        "Status da Rainha",
        max_length=30,
        choices=SimpleStatus.choices,
        default=SimpleStatus.REGULAR,
    )
    q_cf = models.DecimalField(
        "Quantidade de quadros com cria",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
    )
    q_total = models.DecimalField(
        "Quantidade de quadros totais",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
    )
    q_ca = models.DecimalField(
        "Quantidade de quadros com alimento",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
    )
    q_cv = models.DecimalField(
        "Quantidade de quadros com vazio",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
    )

    comments = models.TextField("Observações", max_length=255, default="")
    history = HistoricalRecords()

    def get_changes(self):
        changes = []

        # Obtém todas as versões do histórico ordenadas pela data
        history_versions = self.history.all().order_by("history_date")

        # Compara cada versão com a versão anterior
        for i in range(1, len(history_versions)):
            previous_version = history_versions[i - 1]
            current_version = history_versions[i]

            # Compara os campos do modelo para identificar as alterações
            changed_fields = []

            for field in self._meta.fields:
                field_name = field.name

                previous_value = getattr(previous_version, field_name)
                current_value = getattr(current_version, field_name)

                if previous_value != current_value:
                    changed_fields.append(field_name)

            # Se houver alterações, adiciona à lista de mudanças
            if changed_fields:
                change_info = {
                    "modified": current_version.history_date,
                    "registered_by": current_version.history_user,
                    "changed_fields": changed_fields,
                }
                changes.append(change_info)

        return changes

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
        choices=Hive.Status.choices,
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
    history = HistoricalRecords()

    def __str__(self):
        return str(self.quantity)
