from django.urls import path
from . import views
 

#list of links for the main application

#http://127.0.1:8000/

urlpatterns=[
    path("", views.render_home_main, name="home-page"), #http://127.0.1:8000/ - home page    
    path("about/", views.show_about_page, name="about-page"),
    path("faq/", views.show_faq_page, name="faq-page"), 
    path("news/", views.show_news_page, name="news-page"), 
    path("news/categories/<slug:category_slug>/", views.show_by_category, name="show-by-category"), #http://127.0.1:8000/news/categories/10/ - category page
    path("news/create/", views.create_post, name="create-page"),
    path("news/<slug:slug>/", views.show_post_detail_page, name="news-detail"),
    path("login/", views.show_login_page, name="login-page")
    
]

#{% url "news-detail" post.slug %}
#post.get_absolute_url() 