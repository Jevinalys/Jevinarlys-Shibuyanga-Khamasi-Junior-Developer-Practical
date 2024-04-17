The exercise was implement using python programming language
Developed on python Django Framework
Using SQLite Database

Frontend was developed using HTML 5

The logic for implementation of the solution is in views.py file.
******************************************************
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def taskview(request):
    # Read operation done to sqlite database to read all tasks
    task = Task.objects.all()
    form = TaskForm()

    # User imput validated before being send to the database
    if request.method == 'POST':

        form = TaskForm(request.POST) 

        if form.is_valid():

            form.save()

    # Result displayed in HTML
    context = {'task':task,'form':form}
    return render(request, "index.html", context)