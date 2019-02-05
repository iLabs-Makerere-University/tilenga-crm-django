from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import Company, Employee, Company


class IndexView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'user'
    template_name = 'authentication/users.html'


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'authentication/employee_create.html'
    # fields = ['user', 'company']
    form_class = forms.EmployeeCreateForm 

class CreateUserView(LoginRequiredMixin, generic.CreateView):
    model = User
    context_object_name = 'user'
    template_name = 'authentication/user_create.html'
    fields = ['first_name',  'last_name', 'username', 'email', 'password','is_staff']

class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Company
    context_object_name = 'company'
    template_name = 'authentication/company_create.html'
    fields = ['company_name', 'location', 'description',]

class CompanyListView(LoginRequiredMixin, generic.ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'authentication/company_list.html'

class CompanyDetailView(LoginRequiredMixin, generic.DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'authentication/company_detail.html'

class CompanyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Company
    context_object_name = 'company'
    template_name = 'authentication/company_update.html'
    fields = ['company_name', 'location', 'description',]


    