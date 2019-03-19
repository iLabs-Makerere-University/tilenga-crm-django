from django.db import models
from django.urls import reverse
from order.models import WasteTransferOrder, ServiceInstruction


class LabServiceRequest(models.Model):
    TEST_PARAMETERS = (
        (1, 'Effluent Dischard'),
        (2, 'Sanitary Effluent Discharge'),
        (3, 'Soil Quality'),
        (4, 'Ionising and Radiation')
    )
    waste_tracking_number = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now=True)
    waste_description = models.ForeignKey(
        WasteTransferOrder, on_delete=models.CASCADE)
    order_detail = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    parameters = models.CharField(max_length=20, choices=TEST_PARAMETERS, default=1)
    

    def __str__(self):
        return "Waste Description: {0}".format(self.waste_description.waste_description)

    def get_absolute_url(self):
        return reverse("service:detail", kwargs={"pk": self.pk})

class LabResults(models.Model):
    lab_results = models.FileField(verbose_name='laboratory results')


class TransportServiceRequest(models.Model):
    WASTE_CODE = (
        ('HOO1', 'Aggregate Bitumen'),
        ('H002', 'Chemical Adhesives'),
        ('HOO3', 'Chemical Cleaning'),
        ('H004', 'Chemical Paint'),
        ('H005', 'Chemical Paint Solvents')
    )
    waste = models.CharField(max_length=20, choices=WASTE_CODE, default='H003')
    vehicle_type = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    expected_date = models.DateField()
    inspect_waste = models.BooleanField(default=False)
    collect_waste = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("service:transport-service-detail", kwargs={"pk": self.pk})
    


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=10)
    can_handle_toxic_load = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.vehicle_type)


class ChangeOrderDeviationReport(models.Model):
    """
    When there is a change order, a report is generated that covers
    hazard analysis, process implication analysis (in terms of labour technology, legal implications) and cost analysis
    """
    pass