from django.urls import path

from .views import *

app_name = 'schedule'

urlpatterns = [
    path('list/', schedule_list, name='schedule_list')
]