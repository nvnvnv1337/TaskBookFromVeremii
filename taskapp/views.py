from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .models import Task
from .forms import Taskform
from django.core.cache import cache
from django.views.decorators.cache import never_cache


#def clear_cache():
   # keys = cache.keys('*task_list*')
   # if keys:
     #   for key in keys:
            #cache.delete(key)

    #else:
      #  print('Ключи не найдены')

@never_cache
#@cache_page(60 * 15, key_prefix='task_list')
def task_list(request):
    tasks = Task.objects.all()
    
    return render(request, 'html/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            #clear_cache()
            return redirect('task_list')
        
    else:
        form = Taskform()

    return render(request, 'html/task_create.html', {'form': form})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'html/task_detail.html', {'task': task})

def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            #clear_cache()
            return redirect('task_detail', task_id=task.id)

    else:
        form = Taskform(instance=task)
        return render(request, 'html/task_edit.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        #clear_cache()
        return redirect('task_list')

    else:
        return render(request, 'html/task_delete.html', {'task':task})
        
