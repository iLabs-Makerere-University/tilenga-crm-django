from django.db import models
from django.urls import reverse
from order.models import ServiceInstruction
from authentication.models import Company

class WasteManagementPlan(models.Model):
    service_instruction_number = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    reduce = models.BooleanField()
    reuse = models.BooleanField()
    recycle = models.BooleanField()
    recover = models.BooleanField()
    responsible_treatment_and_disposal = models.BooleanField()
    notes = models.TextField()
    facility = models.ManyToManyField('WasteFacilitie')
    logistics = models.ForeignKey('Vessel', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
    period_of_storage = models.IntegerField(verbose_name='Duration of Storage in Days')
    notes = models.TextField()
    waste_collection_procedure = models.FileField()
    waste_acceptance_procedurie = models.FileField()
    waste_treatment_procedure = models.FileField()
    change_order = models.ForeignKey('ChangeOrder', on_delete=models.CASCADE)
    deviation = models.ForeignKey('Deviation', on_delete=models.CASCADE)


    def get_hierachy(self):
        # return hieracy
        pass

class TechnicalQuery(models.Model):
    technical_query = models.FileField()
    response = models.BooleanField() 
    notes = models.TextField()

class Deviation(models.Model) :
    deviation_request = models.FileField()
    acceptance = models.FileField()

class ChangeOrder(models.Model):
    change_order_request = models.FileField( upload_to=None, max_length=100)
    acceptace_certificate = models.FileField()
    change_order_instruction = models.FileField()

class WasteMangementPlanApproval(models.Model):
    plan = models.ForeignKey(WasteManagementPlan, on_delete=models.CASCADE)
    approved = models.BooleanField()
    comment = models.TextField()
    approved_by = models.CharField(max_length=30)
    date_of_approval = models.DateTimeField(auto_now=True)

class WasteFacilitie(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    code = models.CharField( max_length=50)
    equipment = models.ManyToManyField('Equipment')
    facility_licence = models.FileField()
    location = models.CharField(max_length=20)
    distance_jbr = models.IntegerField(verbose_name='Distance from JBR04')
    distance_ia = models.IntegerField(verbose_name='Distance from Industrial Area')
    waste_criteria = models.FileField(verbose_name='Attach Waste Acceptance Criteria')


class Storage(models.Model):
    facility = models.ForeignKey(WasteFacilitie, on_delete=models.CASCADE)
    duration_of_storage = models.IntegerField(verbose_name='Days of Storage')
    

class Equipment(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("waste:detail-equipment", kwargs={"pk": self.pk})
    

class Vessel(models.Model):
    code = models.CharField(max_length=30)
    description_of_vessel = models.TextField()
    image = models.ImageField()
    truck_license = models.FileField(verbose_name='Truck/ NEMA licence')

