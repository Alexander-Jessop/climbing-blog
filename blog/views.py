"""
Views for the Blog app.

This module contains the views to display lists of published blog posts and
details for individual blog posts.
"""

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, Topic


def list_blogs(request):
    """
    List all published blog posts.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the list of published blogs.
    """
    blogs = Post.objects.filter(published__isnull=False)
    return render(request, 'blog/list_blogs.html', {'blogs': blogs})


def landing_page(request):
    '''
    Landing page for blog app.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the list of published blogs up to 10 and a list of topics up to 10.
    '''
    posts = Post.objects.filter(published__isnull=False)[:10]

    context = {
        'posts': posts
    }

    return render(request, 'blog/landing_page.html', context)


def topic_list(request):
    '''
    Topic list page for blog app.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the list of all topics.
    '''
    all_topics = Topic.objects.all().order_by('name')

    context = {
        'all_topics': all_topics
    }

    return render(request, 'blog/topics.html', context)


def topic_detail(request, slug):
    '''
    Topic detail page for the blog app.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - slug (str): The slug of the topic to display.

    Returns:
    - HttpResponse: Rendered HTML for the topic detail page.
    '''
    topic = get_object_or_404(Topic, slug=slug)

    posts = Post.objects.filter(
        topics=topic,
        published__lte=timezone.now()
    ).order_by('-published')

    context = {
        'topic': topic,
        'posts': posts
    }

    return render(request, 'blog/topic_detail.html', context)


def about(request):
    '''
    About page for blog app.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the about page.
    '''
    return render(request, 'blog/about.html')


def contact(request):
    '''
    Contact page for blog app.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the contact page.
    '''
    return render(request, 'blog/contact.html')
