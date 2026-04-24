from django.shortcuts import render

def show_register_page(request):
    return render(request, "users/register.html")
def show_login_page(request):
    return render(request, "users/login.html")