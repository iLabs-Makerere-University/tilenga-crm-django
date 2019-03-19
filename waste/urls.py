from django.contrib.auth import admin
from django.urls import path, include, reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
   path('create/', views.WasteFacilitieCreateView.as_view(), name='create'),
   path('create/equipment/add/', views.EquipmentCreateView.as_view(), name='add-equipment'),
   path('create/equipment/detail/<int:pk>/', views.EquipmentDetailView.as_view(), name='detail-equipment'),
   path('create/waste-plan/', views.WasteManagementPlanCreateView.as_view(), name='create-plan'),
]

urlpatterns += staticfiles_urlpatterns()