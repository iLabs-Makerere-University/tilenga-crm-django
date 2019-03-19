from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.WasteAcceptanceProcedureCreateView.as_view(), name='create'),
]
