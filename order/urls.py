from django.contrib.auth import admin
from django.urls import path, include, reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.ServiceInstructionListView.as_view(), name='service-list'),
    path('create/', views.ServiceInstructionCreateView.as_view(), name='service-create'),
    path('detail/<int:pk>/', views.WasteTransferDetailView.as_view(), name='order-detail'),
    path('update/<int:pk>/', views.WasteTransferUpdateView.as_view(), name='order-update'),
    path('call-off-orders/', views.ServiceInstructionListView.as_view(), name='call-off-order-list'),
    path('call-off-orders/detail/<int:pk>/', views.ServiceInstructionDetailView.as_view(), name='call-off-order-detail'),
    path('call-off-orders/update/<int:pk>/', views.ServiceInstructionUpdate.as_view(), name='call-off-order-update'),
    path('call-off-orders/process/<int:pk>/', views.process_call_off_order, name="order-process"),
    # path('call-off-orders/delete/<int:pk>/', views.ServiceInstructionDeleteView.as_view(), name='call-off-order-delete'),
]

urlpatterns += staticfiles_urlpatterns()