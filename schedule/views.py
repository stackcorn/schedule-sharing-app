from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Schedule

# Create your views here.

@login_required
def schedule_list(request):
    template_name = 'schedule/list.html'
    params = {}
    schedules = Schedule.objects.filter(user=request.user).all().order_by('created_at').reverse()
    params['schedules'] = schedules
    return render(request, template_name, params)