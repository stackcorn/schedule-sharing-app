from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView
)

from django.urls import reverse_lazy

from .models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'


class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'

class TodoCreate(CreateView):
    model = Todo
    fields = ['title', 'description', 'scheduled_date']
    success_url = reverse_lazy('list')