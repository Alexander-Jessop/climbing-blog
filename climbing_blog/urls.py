"""
URL configuration for climbing_blog project.
"""
from django.contrib import admin
from django.urls import path
from blog.views import landing_page, list_blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page),
    path('blogs/', list_blogs),
]
