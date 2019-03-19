from django.db import models
from waste_treatment.models import WasteTreatmentProcedure


class ServiceInstructionReport(models.Model):
    call_off_order = models.FileField()
    service_instruction = models.FileField()
    waste_management_plan = models.FileField()
    waste_disposal_certificate = models.FileField(
        verbose_name='Waste Disposal Certificate')
    lab_analysis_reports = models.ForeignKey(
        WasteTreatmentProcedure, on_delete=models.CASCADE)
    invoice = models.FileField()

class GeneralReport(models.Model):
    executive_summary = models.FileField( upload_to=None, max_length=100)
    hse_report = models.FileField(upload_to=None, max_length=100)
    waste_mangement_activity_report = models.FileField(upload_to=None, max_length=100)
    contract_admin_report = models.FileField(verbose_name='Contract Administration and Managment Report')
    quality_report = models.FileField(verbose_name='QA QC Report')
    monthy_plans = models.FileField(verbose_name='Monthly Pland and Objectives Report')
