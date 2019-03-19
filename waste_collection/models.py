from django.db import models
from waste.models import ServiceInstruction


class WasteManagementProcedure(models.Model):
    waste_tracking_number = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    waste_collection_procedure_doc = models.FileField()
    permit_to_work = models.FileField()
    site_induction_and_orientation = models.FileField()
    job_hazard_analysis = models.FileField()
    tool_box = models.FileField()
    waste_manifest = models.FileField()
    waste_handover_form = models.FileField(verbose_name='Waste Handover/ Transfer Note')
