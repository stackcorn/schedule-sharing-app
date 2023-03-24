from django.urls import path, include
from .views import Top, Login

app_name ='account'

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('login/', Login.as_view(), name='login'),
]