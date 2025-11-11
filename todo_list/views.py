from django.shortcuts import render, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'todo_list/tasks/task_list.html',
        {'tasks': tasks}
    )
    
def task_detail(request, id):
    task = get_object_or_404(
        Task,
        id = id,
    )
    return render(
        request,
        'todo_list/tasks/task_detail.html',
        {'task': task}
    )
