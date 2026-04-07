from django.http import HttpResponse
from django.shortcuts import render
from .models import HomesSlider

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