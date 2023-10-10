"""
URL configuration for climbing_blog project.

"""
from django.contrib import admin
from django.urls import path

from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
