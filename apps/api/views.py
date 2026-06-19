from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.main.models import Category, FAQ
from .serializers import CategorySerializer, CategoryCreateSerializer, FAQSerializer, CategoryUpdateSerializer
from rest_framework.decorators import parser_classes



# GET, POST, PUT, PATCH, DELETE


@api_view(["GET", "POST",])
def get_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        # categories =[{
        #     "id":c.id,
        #     "name":c.name,
        #     "slug":c.slug,
        #     "created_at":c.created_at,
        #     "updated_at":c.updated_at
        # }
        # for c in categories]

        category_serializer = CategorySerializer(categories, many=True)

        return Response(category_serializer.data)

    # request.data
    # print(request.data)

    serializer = CategoryCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    news_category= serializer.save()  # Category
    new_category_serializer= CategorySerializer(news_category)


    return Response(new_category_serializer.data)

@api_view(["GET", "PATCH", "DELETE"])

def get_update_delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method =="GET":
        serializer=CategorySerializer(category, many=False)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer=CategoryUpdateSerializer(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_category= serializer.save()
        updated_serializer=CategorySerializer(updated_category, many=False)
        return Response(updated_serializer.data)
    
    elif request.method=="DELETE":
        category.delete()
        return Response({"message":"category deleted"})


@api_view(["GET", "POST"])
def get_or_create_faq(request):
    
    if request.method =="POST":
        serializer = FAQSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        faq=serializer.save()
        faq_serializer = FAQSerializer(faq)
        return Response(faq_serializer.data)

    faqs=FAQ.objects.all()
    data=FAQSerializer(faqs, many=True).data 
    return Response(data)