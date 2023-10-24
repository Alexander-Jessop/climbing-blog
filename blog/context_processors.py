"""
Module for navigation-related utilities.
"""


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
            {'name': 'Blogs', 'url': '/blogs'},
            {'name': 'Contact', 'url': '/contact'},
        ]
    }
