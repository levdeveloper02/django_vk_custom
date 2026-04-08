from django.shortcuts import render

def show_register_page(request):
    return render(request, "users/register.html")