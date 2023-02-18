from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    context={
        "todos":todos
    }
    
    return render(request,"list.html",context)

def todo_add(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo_list")
    
    return render(request,"add.html",{"form":form})