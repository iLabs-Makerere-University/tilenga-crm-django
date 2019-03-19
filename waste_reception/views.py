from django.shortcuts import render
from . models import WasteAcceptanceProcedure
from django.views import generic

class WasteAcceptanceProcedureCreateView(generic.CreateView):
    model = WasteAcceptanceProcedure
    template_name = 'waste_reception/waste_acceptance_create.html'
    fields = [
        'waste_tracking_number',
        'waste_acceptance_checklist',
        'waste_manifest_doc',
        'waste_handover_doc',
        'waste_inventory_register'
    ]
