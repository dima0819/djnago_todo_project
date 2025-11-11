from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published', 'changed')
    list_filter = ('status', 'published', 'changed')
    search_fields = ('title', 'body')
