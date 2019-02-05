from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractBaseUser

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse("authentication:company-detail", kwargs={"pk": self.pk})
    
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
