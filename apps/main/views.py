from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#https://127.0.1:8000/main
#hello world

def render_home_main(request):
    return HttpResponse("Hello world!!!")

