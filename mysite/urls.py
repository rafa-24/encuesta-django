from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .views import saluda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saluda', saluda),
    path('polls/', include('polls.url'))
]
