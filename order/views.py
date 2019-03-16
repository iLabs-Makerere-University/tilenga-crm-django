from django.shortcuts import render
from django.views import generic
from .models import WasteTransferOrder, CallOffOrder

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
    template_name = 'order/waste_order_update.html'
    fields = ['waste_description', 'frequency', 'quantity', 'unit_of_measurement', 'total_amount']

class CallOffOrderListView(generic.ListView):
    model = CallOffOrder
    template_name = 'order/call_off_orders_list.html'
    context_object_name = 'call_off_orders'

class CallOffOrderCreateView(generic.CreateView):
    model = CallOffOrder
    template_name = 'order/call_off_order_create.html'
    fields = ['instruction_title', 'contractor_ref', 'company_from', 'representative_name', 'service_description', 'waste_transfer_order',]

class CallOffOrderUpdate(generic.UpdateView):
    model = CallOffOrder
    template_name = 'order/call_off_orders_list.html'
    context_object_name = 'call_off_order'

class CallOffOrderDetailView(generic.DetailView):
    model = CallOffOrder
    template_name = 'order/call_off_orders_list.html'
    context_object_name = 'call_off_order'

def process_call_off_order(request, pk):
    return render(request, 'order/call_off_order_process.html')