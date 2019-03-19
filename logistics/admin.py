from django.contrib import admin
from . models import LogisticsPlan, WasteInspection, WasteCollection, JourneyPlan

class LogisticsPlanAdmin(admin.ModelAdmin):
    pass

class WasteInspectionAdmin(admin.ModelAdmin):
    pass

class WasteCollectionAdmin(admin.ModelAdmin):
    pass

class JourneyPlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(JourneyPlan, JourneyPlanAdmin)
admin.site.register(WasteInspection, WasteInspectionAdmin)
admin.site.register(WasteCollection, WasteCollectionAdmin)
admin.site.register(LogisticsPlan, LogisticsPlanAdmin)

# Register your models here.
