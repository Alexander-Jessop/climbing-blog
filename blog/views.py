"""
Views for the Blog app.

This module contains the views to display lists of published blog posts and
details for individual blog posts.
"""

from django.shortcuts import render
from django.db.models import Count
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
    topics = Topic.objects.annotate(
        post_count=Count('post')).order_by('-post_count')[:10]

    posts = Post.objects.filter(published__isnull=False)[:10]

    context = {
        'topics': topics,
        'posts': posts
    }

    return render(request, 'blog/landing_page.html', context)


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
