from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationFrom, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . import urls
from apps.main.models import Post, PostComment, PostLike, PostDislike, FAQ
from .models import UserProfile


def edit_profile_page(request):
    if request.method == "POST":
        form = EditProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            profile_image=request.FILES.get("profile_image")

            if request.FILES.get("profile_image"):
                request.user.profile.image=profile_image
                request.user.profile.save()
            return redirect("profile-page")
    else:
        form = EditProfileForm(instance=request.user)
    context={
        "form": form
    }
    return render(request, "users/edit_profile.html", context)

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
            user=form.save()
            UserProfile.objects.create(
                user=user,
                image=request.FILES.get("profile_image")
            )
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

def show_profile_page(request):
    posts=Post.objects.filter(author=request.user)


    total_posts_views=[post.views_quantity for post in posts]
    user_posts_comments=[post.statiya.count() for post in posts] #select * from posts where author =1
    # total_likes = [post.likes.user.count() if hasattr(post, 'likes') else 0 for post in posts]
    # total_dislikes=[post.dislikes.user.count() if hasattr(post, 'dislikes') else 0 for post in posts]
    total_likes=[post.likes.user.count() for post in posts] #[2,2,3,4,5]
    total_dislikes=[post.dislikes.user.count() for post in posts]


    context={
        "total_posts": posts.count(), #select * from posts where author =1
        "total_views": sum(total_posts_views),
        "total_comments": sum(user_posts_comments),
        "posts": posts,
        "total_likes": sum(total_likes),
        "total_dislikes": sum(total_dislikes),
    }
    return render(request, "users/profile.html", context)

def show_faq_page(request):
    faqs=FAQ.objects.all()
    # print("working!")
    context={
        "faqs": faqs
    }
    return render(request, "users/faq.html", context)



