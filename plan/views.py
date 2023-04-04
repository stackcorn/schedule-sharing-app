from django.shortcuts import render, redirect
from django.views.generic import (
    ListView ,DetailView, CreateView, DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.
class PlanList(ListView):
    model = Plan
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.order_by('scheduled_date')

class PlanDetail(DetailView):
    model = Plan
    context_object_name = 'plan'

class PlanCreate(CreateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan:list')

class PlanDelete(DeleteView):
    model = Plan
    context_object_name = 'plan'
    success_url = reverse_lazy('plan:list')

@login_required
def signout(request):
    logout(request)
    return redirect('account:signin')