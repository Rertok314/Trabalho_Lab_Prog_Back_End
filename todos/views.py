from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"
# Create your views here.

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")