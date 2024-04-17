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
