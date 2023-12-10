"""
Module for navigation-related utilities.
"""

from django.db.models import Count
from .models import Topic


def navigation(reqeust):
    """
    Navigation list.

    Returns:
        dict: navigation list.
    """
    return {
        'nav_list': [
            {'name': 'Home', 'url': '/'},
            {'name': 'About', 'url': '/about'},
            {'name': 'Topics', 'url': '/topics/'},
            {'name': 'Blogs', 'url': '/blogs'},
            {'name': 'Photo Contest', 'url': '/photo-contest'},
            {'name': 'Contact', 'url': '/contact'},
        ]
    }


def topic_list(request):
    """
    Topic list.

    Returns:
        dict: topic list.
    """
    top_topics = Topic.objects.annotate(
        post_count=Count('post')).order_by('-post_count')[:10]

    return {'topics': top_topics}
