from django import forms
from . models import ServiceInstruction 
from service.models import LabServiceRequest
from waste.models import WasteFacilitie
from authentication.models import Company
from authentication.models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Field, Div
from crispy_forms.bootstrap import (FormActions)


class LabRequestForm(forms.ModelForm):

    class Meta:
        model = LabServiceRequest
        fields = ['waste_description']
        helper = FormHelper()
        helper.form_tag = False


class ServiceInstructionForm(forms.ModelForm):
    # waste_generator = forms.ModelChoiceField(WasteFacilitie.objects.all())
    class Meta:
        model = ServiceInstruction
        fields = [
            'instruction_title',
            'waste_generator',
            'representative_name',
            'service_description',
            'waste_description',
            'waste_code',
            'quantity',
            'unit_of_measurement',
            'waste_profile',
            'msds'
        ]

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'location',
            'description'
        ]