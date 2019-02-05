from django.forms import ModelForm
from . models import User, Employee

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'company']