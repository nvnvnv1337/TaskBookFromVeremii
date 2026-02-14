
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('taskapp.urls')),
    path('/', include('taskapp.urls')),
    path('account/', include('allauth.urls'))
]
