from django.urls import path

from .views import *

app_name = 'schedule'

urlpatterns = [
    path('list/', schedule_list, name='schedule_list'),
    path('detail/<int:pk>', schedule_detail, name='schedule_detail'),
    path('delete/<int:pk>', schedule_delete, name='schedule_delete'),
    path('create/', schedule_create, name='schedule_create'),
    path('signout/', signout, name='signout'),
]