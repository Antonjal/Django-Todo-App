from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


# "index.html" page view. "task_form" is our template key
def index(request):
    form = TaskForm()
    if request.method == "POST":
        #Get the posted form and save it in the database if valid and then redirect the user to the index page
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    tasks = Task.objects.all() # This displays all the Tasks created!
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

# "index.html" task update view and then redirect to the index page 
def update_task(request, pk):
    task = Task.objects.get(id=pk) # Get all task objects based on their IDs
    form = TaskForm(instance=task) # Get a particular task in our form by passing task instance to our form
    if request.method == "POST": # Update the posted form and save it in the database if valid and then redirect the user to the index page
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update_task.html", {"task_edit_form": form})

# "index.html" task delete view and then redirect to the index page 
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")



