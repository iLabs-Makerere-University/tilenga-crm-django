from django.contrib import admin
from . models import WasteManagementPlan, WasteFacilitie, WasteMangementPlanApproval, Equipment, Vessel

class WasteManagementPlanAdmin(admin.ModelAdmin):
    pass

class WasteFacilityAdmin(admin.ModelAdmin):
    pass

class WasteMangementPlanApprovalAdmin(admin.ModelAdmin):
    pass

class EquipmentAdmin(admin.ModelAdmin):
    pass

class VesselAdmin(admin.ModelAdmin):
    pass


admin.site.register(WasteManagementPlan, WasteManagementPlanAdmin)
admin.site.register(WasteFacilitie, WasteFacilityAdmin)
admin.site.register(WasteMangementPlanApproval, WasteMangementPlanApprovalAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Vessel, VesselAdmin)
