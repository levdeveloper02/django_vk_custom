from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationFrom 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . import urls


# def show_register_page(request):
#     if request.method == "POST":
#         form = RegistrationFrom(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "users/register.html")

def show_register_page(request):
    if request.method == "POST":
        print(request.POST)
        form =RegistrationFrom(data=request.POST)
        if form.is_valid(): #proverka na validnost' zapolnenih dannih / check if the form is valid
            form.save() #sohranenie danniye iz formy v baze dannih / the from is save the to the database
            return redirect("login-page") #pereadresatsiya na stranicu login posle uspeshnoy registratsii / redirect to the login page after successful registration
    else :
        form = RegistrationFrom()
    context={
        "form": form
    }
    return render(request, "users/register.html", context)



def show_login_page(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user=form.get_user() #poluchenie pol'zovatelya iz formy / get the user from the form
            if user is not None:
                login(request, user) #vypolnenie funktsii login dlya avtorizatsii pol'zovatelya / perform the login function to authorize the user
                return redirect("home-page")
    else:
        form = LoginForm()
    context={
        "form": form
    }
    return render(request, "users/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("home-page")
