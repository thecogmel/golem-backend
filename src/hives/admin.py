from django.contrib import admin

from .models import Collection, Hive


class HiveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "comments",
        "status",
        "queen_status",
        "q_cf",
        "q_total",
        "q_ca",
        "q_cv",
        "history",
        "created",
        "modified",
    )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "quantity",
        "registered_by",
        "history",
        "created",
        "modified",
    )


admin.site.register(Hive, HiveAdmin)
admin.site.register(Collection, CollectionAdmin)
