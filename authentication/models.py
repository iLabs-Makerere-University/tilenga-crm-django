from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractBaseUser

class Company(models.Model):
    CATEGORIES = (
        ('Lab Services', 'Lab Services'),
        ('Transport Services', 'Transport Services'),
        ('Waste Generator', 'Waste Generator'),
        ('Waste Treatment', 'Waste Treatment'),
        ('Waste Storage', 'Waste Storage')
    )
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES, default='Transport Services', null=True)

    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse("authentication:company-detail", kwargs={"pk": self.pk})
    
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user)
