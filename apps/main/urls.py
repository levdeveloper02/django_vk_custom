from django.urls import path

from . import views

#list of links for the main application

#http://127.0.1:8000/

urlpatterns=[
    path("", views.render_home_main) #http://127.0.1:8000/ - home page    
]
