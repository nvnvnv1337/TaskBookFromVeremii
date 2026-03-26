from django.http import HttpResponse
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.task_list, name='task_list'),
    path('create', views.create_task, name='task_create'),
    path('<int:task_id>', views.task_detail, name='task_detail'),
    path('<int:task_id>/edit', views.task_edit, name='task_edit'),
    path('<int:task_id>/delete', views.task_delete, name='task_delete'),
    
]

