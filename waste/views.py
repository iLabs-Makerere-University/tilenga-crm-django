from django.shortcuts import render
from django.views import generic
from . models import WasteFacilitie, Equipment, WasteManagementPlan


class WasteFacilitieCreateView(generic.CreateView):
    model = WasteFacilitie
    template_name = "waste/waste_facility_create.html"
    fields = [
        'name',
        'code',
        'equipment',
        'facility_licence',
        'location',
        'distance_jbr',
        'distance_ia',
        'waste_criteria'
    ]

class EquipmentCreateView(generic.CreateView):
    model = Equipment
    template_name = "waste/equipment_create_view.html"
    fields = [
        'name', 'description'
    ]

class EquipmentDetailView(generic.DetailView):
    model = Equipment
    template_name = "waste/equipment_detail_view.html"
    context_object_name = 'equipment'


class WasteManagementPlanCreateView(generic.CreateView):
    model = WasteManagementPlan
    template_name = 'waste/waste_management_plan_create.html'
    fields = [
        'service_instruction_number', 'reduce',
        'reuse', 'recycle', 'recover',
        'responsible_treatment_and_disposal',
        'notes','facility',
        'logistics', 'storage',
        'waste_collection_procedure',
        'waste_acceptance_procedurie',
        'waste_treatment_procedure',
        'change_order', 'deviation',
    ]