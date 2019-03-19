from django.contrib import admin
from . models import WasteAcceptanceProcedure

class WasteAcceptanceProcedureAdmin(admin.ModelAdmin):
    pass

admin.site.register(WasteAcceptanceProcedure, WasteAcceptanceProcedureAdmin)
