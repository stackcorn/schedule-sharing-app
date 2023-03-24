from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth.views import LoginView

class Top(TemplateView):
    template_name = 'account/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'