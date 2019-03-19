from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.WasteTreatmentProcedureCreateView.as_view(), name='create'),
]
