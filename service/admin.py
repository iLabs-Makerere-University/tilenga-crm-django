from django.contrib import admin
from . models import Vehicle, LabServiceRequest, LabResults

class LabServiceRequestAdmin(admin.ModelAdmin):
    pass

class VehicleAdmin(admin.ModelAdmin):
    fields = ('vehicle_type', 'registration_number', 'can_handle_toxic_load')

class LabResultsAdmin(admin.ModelAdmin):
    pass



admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(LabServiceRequest, LabServiceRequestAdmin)
admin.site.register(LabResults, LabResultsAdmin)
