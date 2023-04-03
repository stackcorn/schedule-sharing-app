from django import forms
from django.forms import ModelForm

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'description', 'scheduled_date', 'created_by']
        widgets = {
            'scheduled_date': DateInput(),
        }