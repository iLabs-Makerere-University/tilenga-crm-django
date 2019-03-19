from django.shortcuts import render
from django.views import generic
from .models import LabServiceRequest, TransportServiceRequest

class LabServiceCreateView(generic.CreateView):
    model = LabServiceRequest
    template_name = 'service/lab_service_create.html'
    fields = [
        'waste_tracking_number', 
        'waste_description',
        'order_detail',
        'parameters'
    ]

class LabServiceDetailView(generic.DetailView):
    model = LabServiceRequest
    template_name = 'service/lab_service_detail.html'
    context_object_name = 'lab_request'

class LabServiceListView(generic.ListView):
    model = LabServiceRequest
    template_name = 'service/lab_service_list.html'
    context_object_name = 'lab_requests'

class LabServiceUpdateView(generic.UpdateView):
    model = LabServiceRequest
    template_name = 'service/lab_request_update.html'
    context_object_name = 'lab_request'
    fields = ['waste_description']


class TransportServiceListView(generic.ListView):
    model = TransportServiceRequest
    template_name = 'service/transport/transport_service_list.html'
    context_object_name = 'transport_services'


class TransportServiceCreateView(generic.CreateView):
    model = TransportServiceRequest
    template_name = 'service/transport/transport_service_create.html'
    fields = ['inspect_waste', 'collect_waste', 'waste',  'vehicle_type', 'expected_date']

class TransportServiceDetailView(generic.DetailView):
    model = TransportServiceRequest
    template_name = 'service/transport/transport_detail_view.html'
    context_object_name = 'transport_request'