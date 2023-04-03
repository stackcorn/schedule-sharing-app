from django.urls import path
from .views import *

urlpatterns = [
    path('', PlanList.as_view(), name='list'),
    path('detail/<int:pk>', PlanDetail.as_view(), name='detail'),
    path('create/', PlanCreate.as_view(), name='create'),
]