from django.contrib import admin
from . models import WasteTreatmentProcedure

class WasteTreatmentProcedureAdmin(admin.ModelAdmin):
    pass


admin.site.register(WasteTreatmentProcedure, WasteTreatmentProcedureAdmin)

# Register your models here.
