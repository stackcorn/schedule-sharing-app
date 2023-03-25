from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Todo


class TodoHome(TemplateView):
    template_name = 'todo/home.html'

class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'
    ordering = ['scheduled_date'] # 予定日で昇順に並び替える

class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'

class TodoCreate(CreateView):
    model = Todo
    fields = ['title', 'description', 'scheduled_date']
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'scheduled_date']
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('list')

class TodoLogin(LoginView):
    redirect_authenticated_user=True
    template_name='todo/login.html'
    next_page = 'list'

