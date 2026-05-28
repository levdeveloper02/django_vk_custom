from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/users/register/
    path("register/", views.show_register_page, name="register-page"),
    path("login/", views.show_login_page, name="login-page"),
    path("logout/", views.user_logout, name="logout-page"),
    path("me/", views.show_profile_page, name="profile-page"),
    path("faq/", views.show_faq_page, name="faq-page"),
    path("me/edit/", views.edit_profile_page, name="edit-profile-page"),
    path("me/subscribers/", views.show_subscribers_page, name="subscribers-page"),
    path("<int:user_id>/follow/", views.follow_user, name="follow-user"),
    path("<int:user_id>/unfollow/", views.unfollow_user, name="unfollow-user"),

]
