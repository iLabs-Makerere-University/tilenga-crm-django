from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('activate/', views.activate_ivms, name='index'),
    path('create/', views.WasteManagementProcedureCreateView.as_view(), name='create'),
    
]
