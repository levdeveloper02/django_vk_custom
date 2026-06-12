from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from apps.main.models import Category 


#GET, POST, PUT, PATCH, DELETE
@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    categories =[{
        "id":c.id,
        "name":c.name,
        "slug":c.slug,
        "created_at":c.created_at,
        "updated_at":c.updated_at
    }
    for c in categories]
    return Response(categories)

