from django.urls import path

from . import views

#list of links for the main application

#http://127.0.1:8000/

urlpatterns=[
    path("", views.render_home_main, name="home-page"), #http://127.0.1:8000/ - home page    
    path("about/", views.show_about_page, name="about-page"), #http://127.0.1:8000/about/ - about page
    path("fag/", views.show_faq_page, name="faq-page") #http://127.0.1:8000/faq/ - faq page
]
