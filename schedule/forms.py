from django import forms

from .models import Schedule

class CreateScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'content', 'schedule_date']

        widgets = {
            'タイトル': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            '予定日': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
