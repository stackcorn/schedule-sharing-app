from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.
@login_required
def schedule_list(request):
    template_name = 'schedule/list.html'
    user = request.user
    schedules = Schedule.objects.filter(user=user)
    params = {'schedules': schedules,
              'user': user,
              }
    return render(request, template_name, params)