from django.views.generic import ListView

from .models import *

# Create your views here.
class PlanList(ListView):
    model = Plan
    context_object_name = 'plans'