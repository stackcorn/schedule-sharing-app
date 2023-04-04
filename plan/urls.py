from django.urls import path
from .views import *

app_name = 'plan'

urlpatterns = [
    path('', PlanList.as_view(), name='list'),
    path('detail/<int:pk>', PlanDetail.as_view(), name='detail'),
    path('create/', PlanCreate.as_view(), name='create'),
    path('delete/<int:pk>', PlanDelete.as_view(), name='delete'),
    path('signout/', signout, name='signout'),
]