from django.contrib import admin

from .models import Collection, Hive


class HiveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "comments",
        "status",
        "responsible",
        "created",
        "modified",
    )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "quantity",
        "registered_by",
        "created",
        "modified",
    )


admin.site.register(Hive, HiveAdmin)
admin.site.register(Collection, CollectionAdmin)
