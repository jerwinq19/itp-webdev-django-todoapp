from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
import time
# Create your views here.

def Home(request):
    task = Task.objects.all()
    return render(request, 'todolist/home.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        TaskName = request.POST.get('TaskName')
        if TaskName:
            Task.objects.create(taskName=TaskName)
    return redirect('home')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.isDone = not task.isDone
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')