from django.contrib import admin
from .models import ServiceInstructionReport, GeneralReport

class ServiceInstructionReportAdmin(admin.ModelAdmin):
    pass

class GeneralReportAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServiceInstructionReport, ServiceInstructionReportAdmin)
admin.site.register(GeneralReport, GeneralReportAdmin)
# Register your models here.
