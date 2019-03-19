from django.db import models
from waste.models import ServiceInstruction

class WasteAcceptanceProcedure(models.Model):
    waste_tracking_number = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    waste_acceptance_checklist = models.FileField()
    waste_manifest_doc = models.FileField()
    waste_handover_doc = models.FileField(verbose_name='waste handover/ transfer note')
    waste_inventory_register = models.FileField()

