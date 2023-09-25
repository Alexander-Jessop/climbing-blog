'''
View pages for the app Index
'''

from django.shortcuts import render

# Create your views here.


def index(request):
    '''
    This is the index page.
    '''
    url_list = [
        {"url_name": "Index", "url_link": "/"},
        {"url_name": "Admin", "url_link": "admin/"},
    ]
    return render(
        request,
        "index/index.html",
        {
            "url_list": url_list,
        },
    )
