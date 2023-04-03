from django.views.generic import ListView ,DetailView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.
class PlanList(ListView):
    model = Plan
    context_object_name = 'plans'

class PlanDetail(DetailView):
    model = Plan
    context_object_name = 'plan'

class PlanCreate(CreateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('list')