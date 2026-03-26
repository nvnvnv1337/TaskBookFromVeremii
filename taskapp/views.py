from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .models import Task
from .forms import Taskform
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions


@login_required
def home(request):
    return render(request, 'taskapp/home.html')

@login_required  
def task_list(request):
    tasks = CacheMeneger.get_tasks(request.user.id)
    return render(request, 'taskapp/task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            CacheMeneger.clear_cache(request.user.id)
            form.save()
            #clear_cache()
            return redirect('task_list')
        
    else:
        form = Taskform()

    return render(request, 'taskapp/task_create.html', {'form': form})
@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'taskapp/task_detail.html', {'task': task})
@login_required
def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            CacheMeneger.clear_cache(request.user.id)
            form.save()
            #clear_cache()
            return redirect('task_detail', task_id=task.id)

    else:
        form = Taskform(instance=task)
        return render(request, 'taskapp/task_edit.html', {'form': form, 'task': task})
@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        CacheMeneger.clear_cache(request.user.id)
        task.delete()
        #clear_cache()
        return redirect('task_list')

    else:
        return render(request, 'taskapp/task_delete.html', {'task':task})



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else: return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# принцип SRP
class CacheMeneger:
    timeout = 150
    @staticmethod
    def get_tasks(user_id):
        cache_key = f'task_list_by{user_id}'
        tasks = cache.get(cache_key)
        if not tasks:
            tasks = Task.objects.filter(user=user_id)
            cache.set(cache_key, tasks, CacheMeneger.timeout)
        return tasks
    @staticmethod
    def clear_cache(user_id):
        cache_key = f'task_list_by{user_id}'
        cache.delete(cache_key)

        