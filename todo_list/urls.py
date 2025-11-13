from django.urls import path
from .views import task_list, task_detail, task_create, TaskUpdateView

app_name = 'todo_list'

urlpatterns = [
    path('', task_list, name='task_list'),
    path('tasks/<int:id>/', task_detail, name='task_detail'),
    path('tasks/create/', task_create, name = 'task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
]