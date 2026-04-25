from django.urls import path
from . import views

urlpatterns=[
    path("register/", views.show_register_page, name="register-page"), #http://127.0.0.1:8000/users/register/
    path("login/", views.show_login_page, name="login-page"), #http://127.0.0.1:8000/users/login/
    path("logout/", views.user_logout, name="logout-page") #http://127.0.0.1:8000/users/logout/
]