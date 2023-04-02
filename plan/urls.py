from django.urls import path
from .views import *

urlpatterns = [
    path('', PlanList.as_view(), name='list'),
]