
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskapp.urls')),
    path('api/', include('taskapp.api_urls')),
    path('accounts/', include('allauth.urls'))
]
