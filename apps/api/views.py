from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.main.models import Category, FAQ
from .serializers import CategorySerializer, CategoryCreateSerializer, FAQSerializer, FAQCreateSerializer
from rest_framework.parsers import MultiPartParser
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


@api_view(["GET", "POST"])
def get_or_create_faq(request):
    if request.method =="POST":
        serializer = FAQCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception="True")
        faq=serializer.save()
        faq_serializer = FAQSerializer(faq)
        return Response(faq_serializer.data)

    faqs=FAQ.objects.all()
    data=FAQSerializer(faqs, many=True).data 
    return Response(data)