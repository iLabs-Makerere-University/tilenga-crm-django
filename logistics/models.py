from django.db import models
from waste.models import Vessel, ServiceInstruction


class LogisticsPlan(models.Model):
    waste_inspection = models.ForeignKey('WasteInspection', on_delete=models.CASCADE)
    waste_collection = models.ForeignKey('WasteCollection', on_delete=models.CASCADE)
    waste_tracking_number = models.ForeignKey(ServiceInstruction, on_delete=models.CASCADE)
    approval = models.ForeignKey('LogisticsPlan', on_delete=models.CASCADE)

class LogistsPlanApproval(models.Model):
    approval = models.BooleanField()
    approved_by = models.CharField(max_length=30)
    comments = models.TextField()
    date_of_approval = models.DateTimeField(auto_now=True)

class WasteInspection(models.Model):
    approval = models.BooleanField()
    journey_management_form = models.FileField()
    driving_permit = models.FileField()
    fitness_certificate = models.FileField()
    vehicle_and_inspection_form = models.FileField()
    journey_risk_assessment = models.FileField()
    journey_emergency_reponse_plan = models.FileField()
    truck_nema_licence = models.FileField()
    journey_plan = models.ManyToManyField('JourneyPlan')
    date_of_approval = models.DateTimeField(auto_now=True)

class WasteCollection(models.Model):
    approved = models.BooleanField()
    journey_management_form = models.FileField()
    risk_assessment = models.FileField()
    driving_permit = models.FileField()
    fitness_certificate = models.FileField()
    vehicle_and_inspection_form = models.FileField()
    journey_risk_assessment = models.FileField()
    journey_emergency_reponse_plan = models.FileField()
    truck_nema_licence = models.FileField()
    journey_plan = models.ManyToManyField('JourneyPlan')
    date_of_approval = models.DateTimeField(auto_now=True)

class CollectionService(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    journey_plan = models.ForeignKey('JourneyPlan', on_delete=models.CASCADE)

class JourneyPlan(models.Model):
    date = models.DateField()
    departure_time = models.TimeField()
    departure_from = models.CharField(max_length=20, verbose_name='From')
    departure_to= models.CharField(max_length=20, verbose_name='To')
    distance = models.IntegerField()
    

