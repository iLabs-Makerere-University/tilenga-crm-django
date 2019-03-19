from django.shortcuts import render
from django.views import generic
from . models import WasteInspection

class WasteInspectionCreateView(generic.CreateView):
    model = WasteInspection
    template_name = 'logistics/inspection_create.html'
    fields = [
        'approval',
        'journey_management_form',
        'driving_permit',
        'fitness_certificate',
        'vehicle_and_inspection_form',
        'journey_risk_assessment',
        'journey_emergency_reponse_plan',
        'truck_nema_licence',
        'journey_plan',
    ]

