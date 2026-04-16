from django.http import HttpResponse
from django.shortcuts import render
from .models import HomesSlider,Category,Post

# Create your views here.

#https://127.0.1:8000/main
#hello world

# select * from main_homesslider;

def render_home_main(request):
    # return HttpResponse("Hello world!!!")
    slider_photos = HomesSlider.objects.all() #select * from main_homesslider;
    context = {
        "slider_photos": slider_photos
    }
    return render(request, "main/index.html", context=context)

def show_about_page(request):
    return render(request, "main/about.html")

def show_faq_page(request):
    return render(request, "main/faq.html")

categories_data=["Sports", "Politics","World","Space","Science"]


def show_news_page(request):
    categories_data= Category.objects.all() #select * from main_categories;
    posts=Post.objects.all().values("title", "short_description", "preview") #select * from main_posts
    print(request.__dict__)


    context={
        "categories_data": categories_data,
        "posts":posts
    }
    return render(request, "main/news.html", context)

#http://127.0.0.1:8000/news/categories/10

def show_by_category(request, category_slug):
    categories= Category.objects.all() #select * from main_categories;

    # print(request.__dict__)
    # print(request.resolver_match)
    print(request.resolver_match.kwargs.get("category_slug"))

    #you can get an error if: 1)more than 1 value is recieved 2)no value is received
    category=Category.objects.get(slug=category_slug) # select * from main_categories where slug = ? 
    
    #.filter() 
    
    context={
        "categories_data": categories,
        "category": category
    }
    return render(request, "main/news.html", context)