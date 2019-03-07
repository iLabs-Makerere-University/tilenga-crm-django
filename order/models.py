from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.models import Company
from datetime import datetime


class CallOffOrder(models.Model):
    instruction_title = models.CharField(max_length=100)
    call_off_order_number = id
    contractor_ref = models.CharField(max_length=30)
    company_from = models.ForeignKey(Company, on_delete=models.CASCADE)
    representative_name = models.ForeignKey(User, on_delete=models.CASCADE)
    service_description = models.TextField()
    total_value = models.IntegerField()
    waste_transfer_order = models.ForeignKey('WasteTransferOrder', on_delete=models.CASCADE)

    def __str__(self):
        return self.instruction_title
    



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
    

