'''
Register blog models with the admin site.
'''

from django.contrib import admin
from . import models

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    '''
    Admin representation for the Comment model.
    '''

    list_display = ('name', 'email', 'text', 'approved', 'created')
    search_fields = ('name', 'email', 'text')
    list_filter = ('approved',)


admin.site.register(models.Comment, CommentAdmin)


class CommentInline(admin.TabularInline):
    '''
    Inline representation for the Comment model in the Post admin view.
    '''

    model = models.Comment
    fields = ('name', 'email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text')
    extra = 0


class PostAdmin(admin.ModelAdmin):
    '''
    Represents a blog post in the admin site.
    '''

    list_display = ('title', 'created', 'updated')
    ordering = ('created',)
    search_fields = ('title', 'author__username',
                     'author__first_name', 'author__last_name')
    list_filter = ('status', 'topics')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]


admin.site.register(models.Post, PostAdmin)


class TopicAdmin(admin.ModelAdmin):
    '''
    Represents a topic in the admin site.
    '''

    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Topic, TopicAdmin)
