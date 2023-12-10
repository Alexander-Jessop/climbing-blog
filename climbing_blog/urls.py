"""
URL configuration for climbing_blog project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import (
    landing_page,
    list_blogs,
    about,
    contact,
    topic_list,
    topic_detail,
    photo_contest_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home'),
    path('blogs/', list_blogs, name='list_blogs'),
    path('about/', about, name='about'),
    path('topics/', topic_list, name='topics'),
    path('contact/', contact, name='contact'),
    path('topics/<slug:slug>/', topic_detail, name='topic_detail'),
    path('photo-contest/', photo_contest_view, name='photo_contest'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
