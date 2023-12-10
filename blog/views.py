"""
Views for the Blog app.

This module contains the views to display lists of published blog posts and
details for individual blog posts.
"""

from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.contrib import messages
from .models import Post, Topic
from .forms import PhotoSubmissionForm


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


def photo_contest_view(request):
    """
    View for submitting photos to the photo contest.

    This view handles the submission of photo contest entries. It creates a form instance
    using the PhotoSubmissionForm when a GET request is made. Upon POST request, it
    validates and saves the form, then redirects or shows a success message.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered HTML for the photo contest submission form, or a redirect
                    to a success page upon successful form submission.
    """
    if request.method == 'POST':
        form = PhotoSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you! Your photo submission has been received.')
            return redirect('photo_contest')
    else:
        form = PhotoSubmissionForm()
    return render(request, 'blog/photo_contest.html', {'form': form})
