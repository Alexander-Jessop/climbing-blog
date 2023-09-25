'''
Django App Config for index app
'''

from django.apps import AppConfig


class IndexConfig(AppConfig):
    '''
    Configuration for index app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
