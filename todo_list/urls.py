from django.urls import path
from .views import task_list, task_detail

app_name = 'todo_list'

urlpatterns = [
    path('', task_list, name='task_list'),
    path('tasks/<int:id>/', task_detail, name='task_detail')
]