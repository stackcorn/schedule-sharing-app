from django.shortcuts import redirect
from django.views.generic import (
    ListView ,DetailView, CreateView, DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

# Create your views here.
class PlanList(LoginRequiredMixin, ListView):
    model = Plan
    context_object_name = 'plans'
    login_url = 'account/signin/'

    def get_queryset(self):
        return Plan.objects.order_by('scheduled_date')

class PlanDetail(LoginRequiredMixin, DetailView):
    model = Plan
    context_object_name = 'plan'
    login_url = 'account/signin/'

class PlanCreate(LoginRequiredMixin, CreateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan:list')
    login_url = 'account/signin/'

class PlanDelete(LoginRequiredMixin, DeleteView):
    model = Plan
    context_object_name = 'plan'
    success_url = reverse_lazy('plan:list')
    login_url = 'account/signin/'

@login_required
def signout(request):
    logout(request)
    return redirect('account:signin')