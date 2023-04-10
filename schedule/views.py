from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Schedule
from .forms import CreateScheduleForm

# Create your views here.

@login_required
def schedule_list(request):
    template_name = 'schedule/list.html'
    params = {}
    schedules = Schedule.objects.filter(user=request.user).all().order_by('created_at').reverse()
    params['schedules'] = schedules
    return render(request, template_name, params)

@login_required
def schedule_detail(request, pk):
    template_name = 'schedule/detail.html'
    params = {}
    schedule = get_object_or_404(Schedule, id=pk, user=request.user)
    params['schedule'] = schedule
    return render(request, template_name, params)

@login_required
def schedule_delete(request, pk):
    template_name = 'schedule/confirm_delete.html'
    params = {}
    schedule = get_object_or_404(Schedule, id=pk, user=request.user)
    params['schedule'] = schedule
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule:schedule_list')
    else:
        return render(request, template_name, params)
    
@login_required
def schedule_create(request):
    template_name = 'schedule/schedule_create.html'
    form = CreateScheduleForm(request.POST or None)
    params = {'form': form}
    if form.is_valid():
        schedule = form.save(commit=False)
        schedule.user = request.user
        schedule.save()
        return redirect('schedule:schedule_list')
    else:
        return render(request, template_name, params)