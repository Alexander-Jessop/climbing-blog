'''
Register blog models with the admin site.
'''

from django.contrib import admin
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    '''Represents a blog post in the admin site.'''
    list_display = ('title', 'created', 'updated')
    ordering = ('created',)
    search_fields = ('title', 'author__username',
                     'author__first_name', 'author__last_name')
    list_filter = ('status', 'topics')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Post, PostAdmin)


class TopicAdmin(admin.ModelAdmin):
    '''Represents a topic in the admin site.'''
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Topic, TopicAdmin)
