from django.contrib import admin
from .models import Empresa, Gestion, Recordatorio
from import_export.admin import ImportExportModelAdmin

admin.site.register(Gestion)
admin.site.register(Recordatorio)
@admin.register(Empresa)
class userdat(ImportExportModelAdmin):
    pass