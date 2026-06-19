from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.get_categories),
    path("categories/<int:category_id>/", views.get_update_delete_category),
    path("faqs/", views.get_or_create_faq),
]