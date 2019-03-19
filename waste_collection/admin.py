from django.contrib import admin
from . models import WasteManagementProcedure


class WasteManagementProcedureAdmin(admin.ModelAdmin):
    pass

admin.site.register(WasteManagementProcedure, WasteManagementProcedureAdmin)
