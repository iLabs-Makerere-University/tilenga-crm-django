from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.models import Company
from datetime import datetime


class ServiceInstruction(models.Model):
    WASTE_TYPE = (
        ('H', "Hazadous"),
        ("NH", 'Non Hazadous')
    )
    WASTE_CODE = (
        ('HOO1', 'Aggregate Bitumen'),
        ('H002', 'Chemical Adhesives'),
        ('HOO3', 'Chemical Cleaning'),
        ('H004', 'Chemical Paint'),
        ('H005', 'Chemical Paint Solvents')
    )

    service_instruction_number = models.CharField(max_length=10)
    instruction_title = models.CharField(max_length=100)
    waste_tracking_number = models.CharField(max_length=30, null=True)
    waste_generator = models.ForeignKey(Company, on_delete=models.CASCADE)
    representative_name = models.ForeignKey(User, on_delete=models.CASCADE)
    service_description = models.TextField()
    waste_description = models.CharField(max_length=10, choices= WASTE_TYPE, default='H')
    waste_code = models.CharField(max_length=10, choices=WASTE_CODE, default='H001')
    quantity = models.PositiveIntegerField()
    unit_of_measurement = models.CharField(max_length=10)
    waste_profile = models.FileField(verbose_name='waste profile')
    msds = models.FileField(verbose_name='MSDS')

    def __str__(self):
        return self.instruction_title
    
    def save(self):
        self.now = datetime.now()
        self.service_instruction_number =  "{}/{}/{}/{}".format(self.now.year, self.now.month, self.now.day, self.id)
        super(ServiceInstruction, self).save()
    
    def get_absolute_url(self):
        return reverse("order:call-off-order-detail", kwargs={"pk": self.pk})
    
    
    



class WasteTransferOrder(models.Model):
    now = datetime.now()
    waste_description = models.TextField()
    frequency = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    unit_of_measurement = models.CharField(max_length=10)
    total_amount = models.PositiveIntegerField()
    
    @property
    def waste_transfer_note_number(self):
        self.now = datetime.now()
        return "{0}/{1}/{2}/{3}".format(self.now.day, self.now.month, self.now.year, self.id)
            
    def __str__(self):
        return "{}".format(self.waste_transfer_note_number)
    
    def get_absolute_url(self):
        return reverse("order:order-detail", kwargs={"pk": self.pk})
    

    