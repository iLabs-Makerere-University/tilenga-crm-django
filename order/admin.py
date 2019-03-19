from django.contrib import admin
from .models import ServiceInstruction, WasteTransferOrder

class ServiceInstructionAdmin(admin.ModelAdmin):
    pass

class WasteTransferOrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(ServiceInstruction, ServiceInstructionAdmin)
admin.site.register(WasteTransferOrder, WasteTransferOrderAdmin)
