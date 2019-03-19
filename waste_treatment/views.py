from django.shortcuts import render
from . models import WasteTreatmentProcedure
from django.views import generic


class WasteTreatmentProcedureCreateView(generic.CreateView):
    model = WasteTreatmentProcedure
    template_name = 'waste_treatment/treatment_plan_create.html'
    fields = [
        'waste_tracking_number',
        'waste_treatement_log',
        'flue_gas_log',
        'discharge_log',
        'residue_waste_log',
        'residue_waste_analysis_report',
        'effluent_analysis_report',
        'waste_disposal_certificate',
        'waste_handover_doc',
        'stabilization_report'
    ]
