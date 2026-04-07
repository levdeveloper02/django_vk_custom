from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main' #path to the application folder, relative to the project
    verbose_name="Main Application" #application name in english
