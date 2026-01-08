from django.contrib import admin
from .models import Task

@admin.register(Task)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created_at', 'user']
    list_filter = ['title', 'description', 'completed', 'created_at', 'user']
    search_fields = ['title', 'description']