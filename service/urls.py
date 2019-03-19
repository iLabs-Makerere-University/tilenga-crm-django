from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('', views.LabServiceListView.as_view(), name='index'),
    path('create/', views.LabServiceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.LabServiceUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.LabServiceDetailView.as_view(), name='detail'),
    path('transport/', views.TransportServiceListView.as_view(), name='transport-service-list'),
    path('transport/create/', views.TransportServiceCreateView.as_view(), name='transport-service-create'),
    path('transport/detail/<int:pk>/', views.TransportServiceDetailView.as_view(), name='transport-service-detail'),
]
