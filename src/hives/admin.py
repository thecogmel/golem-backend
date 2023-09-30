from django.contrib import admin

from .models import Hive


class HiveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "status",
        "responsible",
        "created",
        "modified",
    )


admin.site.register(Hive, HiveAdmin)
