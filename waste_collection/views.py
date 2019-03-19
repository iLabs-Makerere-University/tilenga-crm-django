from django.shortcuts import render, HttpResponse
from django.views import generic
from . models import WasteManagementProcedure

def activate_ivms(request):
    return render(request, 'waste_collection/activate_ivms.html', context=None)


class WasteManagementProcedureCreateView(generic.CreateView):
    model = WasteManagementProcedure
    context_object_name = 'waste_collection_object'
    template_name = "waste_collection/waste_collection_create.html"
    fields = [
        'waste_tracking_number',
        'waste_collection_procedure_doc',
        'permit_to_work',
        'site_induction_and_orientation',
        'job_hazard_analysis',
        'tool_box',
        'waste_manifest',
        'waste_handover_form'
    ]