from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskCreateForm
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

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


def task_create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:task_list')
    else:
        form = TaskCreateForm()
    return render(
        request,
        'todo_list/tasks/task_create.html',
        {'form': form}
    )   
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'body', 'status']
    template_name = 'todo_list/tasks/task_update.html'
    success_url = reverse_lazy('todo:task_list')
    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo_list/tasks/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')