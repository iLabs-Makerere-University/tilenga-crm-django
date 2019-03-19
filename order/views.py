from django.shortcuts import render, HttpResponse, reverse, render_to_response
from django.views import generic
from .models import WasteTransferOrder, ServiceInstruction
from service.models import TransportServiceRequest
from authentication.models import Company
from . forms import LabRequestForm, ServiceInstructionForm, CompanyForm
from django.forms.models import inlineformset_factory, modelform_factory

company_form_fields = modelform_factory(Company, CompanyForm)


class WasteTransferCreateView(generic.CreateView):
    model = WasteTransferOrder
    template_name = 'order/waste_order_create.html'
    fields = ['waste_description', 'frequency', 'quantity', 'unit_of_measurement', 'total_amount']

class WasteTransferListView(generic.ListView):
    model = WasteTransferOrder
    template_name = 'order/waste_order_list.html'
    context_object_name = 'waste_orders'

class WasteTransferDetailView(generic.DetailView):
    model = WasteTransferOrder
    template_name = 'order/waste_order_detail.html'
    context_object_name = 'waste_order'

class WasteTransferUpdateView(generic.UpdateView):
    model = WasteTransferOrder
    context_object_name = 'call_off_order'
    template_name = 'order/waste_order_update.html'
    fields = ['waste_description', 'frequency', 'quantity', 'unit_of_measurement', 'total_amount']

class ServiceInstructionListView(generic.ListView):
    model = ServiceInstruction
    template_name = 'order/call_off_orders_list.html'
    context_object_name = 'call_off_orders'

class ServiceInstructionCreateView(generic.CreateView):
    model = ServiceInstruction
    template_name = 'order/call_off_order_create.html'
    form_class = ServiceInstructionForm

    # def get(self, request, *args, **kwargs):
    #     service_request = ServiceInstructionForm()
    #     service_request.prefix = 'service_request_form'
    #     return render_to_response(self.get_context_data({'service_request_form': service_request}))
    
    # def post(self, request, *args, **kwargs):
    #     service_request_form = ServiceInstructionForm()
    #     if service_request_form.is_valid():
    #         service_request_form.save()
    #         return HttpResponse('Got that right')
    #     else: 
    #         return self.form_invalid(service_request_form, **kwargs)
    
    # def form_invalid(self, service_request_form, **kwargs):
    #     service_request_form.prefix = 'service_request_form'
    #     return self.render_to_response({'service_request_form': service_request_form})

class ServiceInstructionUpdate(generic.UpdateView):
    model = ServiceInstruction
    template_name = 'order/call_off_order_update.html'
    context_object_name = 'call_off_order'
    fields = [
        'instruction_title', 'service_description',
        'waste_description', 'quantity',
        'unit_of_measurement', 
    ]

class ServiceInstructionDetailView(generic.DetailView):
    model = ServiceInstruction
    template_name = 'order/call_off_order_detail.html'
    context_object_name = 'call_off_order'


class ProcessLabRequestCreateView(generic.FormView):
    # model = TransportServiceRequest
    template_name = 'service/transport/sub_pages/lab_services/_lab_service_create.html'
    def get(self, request, *args, **kwargs):
        lab_request_form = LabRequestForm()
        lab_request_form.prefix = 'lab_request_form'
        return self.render_to_response(self.get_context_data({'lab_request_form':lab_request_form}))

    def post(self, requst, *args, **kwargs):
        lab_request_form = LabRequestForm()
        if lab_request_form.is_valid():
            return HttpResponse('Got that right')
        else:
            return self.form_invalid(lab_request_form, **kwargs)
    
    def form_invalid(self, lab_request_form, **kwargs):
        lab_request_form.prefix = 'lab_request_form'
        return self.render_to_response({'lab_request_form': lab_request_form})

def process_call_off_order(request, pk):
    return render(request, 'order/call_off_order_process.html')