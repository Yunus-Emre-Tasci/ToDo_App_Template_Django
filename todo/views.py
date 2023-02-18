from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

class TodoListView(ListView):
    model=Todo

class TodoCreateView(CreateView):
    model=Todo
    form_class=TodoForm
    success_url=reverse_lazy("todo_list")    