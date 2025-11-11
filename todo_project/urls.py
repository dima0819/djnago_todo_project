from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_list/', include('todo_list.urls', namespace = 'todo')),
]
