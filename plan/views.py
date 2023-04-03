from django.views.generic import ListView ,DetailView

from .models import *

# Create your views here.
class PlanList(ListView):
    model = Plan
    context_object_name = 'plans'

class PlanDetail(DetailView):
    model = Plan
    context_object_name = 'plan'