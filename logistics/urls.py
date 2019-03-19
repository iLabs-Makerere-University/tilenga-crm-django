from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.WasteInspectionCreateView.as_view(), name='create'),
]
