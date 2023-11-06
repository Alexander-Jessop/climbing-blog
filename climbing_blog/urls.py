"""
URL configuration for climbing_blog project.
"""
from django.contrib import admin
from django.urls import path
from blog.views import landing_page, list_blogs, about, contact, topic_list, topic_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page),
    path('blogs/', list_blogs),
    path('about/', about),
    path('topics/', topic_list, name='topics'),
    path('contact/', contact),
    path('topics/<slug:slug>/', topic_detail, name='topic_detail')
]
