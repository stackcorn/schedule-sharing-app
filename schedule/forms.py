from django import forms

from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'content', 'schedule_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'schedule_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
