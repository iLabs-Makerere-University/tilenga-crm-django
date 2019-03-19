from django.db import models
from waste.models import ServiceInstruction

class WasteTreatmentProcedure(models.Model):
    waste_tracking_number = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    waste_treatement_log = models.FileField()
    flue_gas_log = models.FileField()
    discharge_log = models.FileField(verbose_name='Discharge Log (Gas/ Waste water)')
    residue_waste_log = models.FileField()
    residue_waste_analysis_report = models.FileField()
    effluent_analysis_report = models.FileField()
    waste_disposal_certificate = models.FileField()
    waste_handover_doc = models.FileField(verbose_name='Secondary waste handover/ transfer note')
    stabilization_report = models.FileField(verbose_name='Stabilization and Solidification Report')
