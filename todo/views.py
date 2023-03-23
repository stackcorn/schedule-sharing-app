from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.urls import reverse_lazy

from .models import Todo


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