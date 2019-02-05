from django.contrib.auth import views as auth_views
from django.contrib.auth import admin
from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name="authentication/registration/login.html",
        redirect_authenticated_user = True,
        extra_context={
            # 'next': 'auth/company/',
            'next': 'auth/company/',
            'title': 'Login',
        }
    ),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('employees/', views.EmployeeCreateView.as_view(), name='create-employee'),
    path('user/create/', views.CreateUserView.as_view(), name='create-user'),
    path('company/', views.CompanyListView.as_view(), name='company-list'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail'),
    path('company/create/', views.CompanyCreateView.as_view(), name='create-company'),
    path('company/update/<int:pk>/', views.CompanyUpdateView.as_view(), name='company-update'),
]
