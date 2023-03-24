from django.urls import path, include
from .views import TopView

app_name ='account'

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]