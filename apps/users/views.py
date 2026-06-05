from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationFrom, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . import urls
from apps.main.models import Post, PostComment, PostLike, PostDislike, FAQ
from .models import Subscriber, UserProfile
from django.contrib.auth.models import User
from django.http import JsonResponse


def edit_profile_page(request):
    if request.method == "POST":
        form = EditProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            profile_image=request.FILES.get("profile_image")

            if request.FILES.get("profile_image"):

                profil,_=UserProfile.objects.get_or_create(user=request.user)
                profil.image=profile_image
                profil.save()
                # request.user.profile.image=profile_image
                # request.user.profile.save()
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

from django.urls import reverse
from django.shortcuts import redirect


def show_register_page(request):
    if request.method == "POST":
        form = RegistrationFrom(data=request.POST)
        
        if form.is_valid():
            # 1. Kullanıcıyı bir kere kaydet ve kimliğini (user) al
            user = form.save()
            
            # 2. Kullanıcının profilini oluştur
            UserProfile.objects.create(
                user=user,
                image=request.FILES.get("profile_image")
            )
            
            # 3. Yönlendireceğimiz VIP rotayı bul
            base_url = reverse("tg-bot-page")
            
            # 4. Eski login yönlendirmesini çöpe atıp, YENİ kullanıcının ID'si ile bot sayfasına yolla!
            return redirect(f"{base_url}?user_id={user.id}")
            
    else:
        form = RegistrationFrom()
        
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

# def show_register_page(request):

#     base_url=reverse("tg-bot-page")  

#     if request.method == "POST":
#         print(request.POST)
#         form =RegistrationFrom(data=request.POST)
#         if form.is_valid(): #proverka na validnost' zapolnenih dannih / check if the form is valid
#             user=form.save()
#             UserProfile.objects.create(
#                 user=user,
#                 image=request.FILES.get("profile_image")
#             )
#             form.save() #sohranenie danniye iz formy v baze dannih / the from is save the to the database
#             return redirect("login-page") #pereadresatsiya na stranicu login posle uspeshnoy registratsii / redirect to the login page after successful registration
#     else :
#         form = RegistrationFrom()
#     context={
#         "form": form
#     }
#     return render(request, "users/register.html", context)
# return redirect(f"{base_url}?user_id={request.user.id}") 



# def show_login_page(request):
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             # log in the user
#             user=form.get_user() #poluchenie pol'zovatelya iz formy / get the user from the form
#             if user is not None:
#                 login(request, user) #vypolnenie funktsii login dlya avtorizatsii pol'zovatelya / perform the login function to authorize the user
#                 return redirect("home-page")
#     else:
#         form = LoginForm()
#     context={
#         "form": form
#     }
#     return render(request, "users/login.html", context)

def show_login_page(request):
    if request.method == "POST":
        form= RegistrationFrom(data=request.POST)
        if form.is_valid():
            user=form.save()
            UserProfile.objects.create(
                user=user,
                image=request.FILES.get("profile_image")
            )



            return redirect(f"/tg-bot/confirmation/?user_id={user.id}")
    else:
        form = RegistrationFrom()
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
    total_likes=[post.likes.user.count() if hasattr(post, 'likes') else 0 for post in posts] #[2,2,3,4,5]
    total_dislikes=[post.dislikes.user.count() if hasattr(post, 'dislikes') else 0 for post in posts]

    subscriber_total=request.user.profile.subscribers.subscriber.count() if hasattr(request.user.profile, 'subscribers') else 0


    context={
        "total_posts": posts.count(), #select * from posts where author =1
        "total_views": sum(total_posts_views),
        "total_comments": sum(user_posts_comments),
        "posts": posts,
        "total_likes": sum(total_likes),
        "total_dislikes": sum(total_dislikes),
        "subscriber_total": subscriber_total    
    }
    return render(request, "users/profile.html", context)

def show_faq_page(request):
    faqs=FAQ.objects.all()
    # print("working!")
    context={
        "faqs": faqs
    }
    return render(request, "users/faq.html", context)


def show_subscribers_page(request):


    current_user=request.user

    subscribers= Subscriber.objects.all() #[Subscriber, ]
    # print(subscribers)

    following_users=[]
    for sub in subscribers:
        if current_user in sub.subscriber.all():
            following_users.append(sub)
        # print(sub.user_profile, sub.subscriber.all())
        # print(following_users)
    following_users = [sub.user_profile.user for sub in following_users]

    context={
        "following_users": following_users
    }

    return render(request, "users/subscribers.html", context)    





def follow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id) #polucayem pol'zovatelya  na kotorogo hotim podpisatsya / get the user we want to subscribe
    current_user=request.user #pol'zovatel', kotorıy hocet podpisatsya / the user who wants to subscribe

    target_profile , _ = UserProfile.objects.get_or_create(user=user_to_follow) #polucayem pol'zovatelya  na kotorogo hotim podpisatsya / get the user we want to subscribe
    
    subscriber_file , _= Subscriber.objects.get_or_create(user_profile=target_profile)

    subscriber_file.subscriber.add(current_user) #dobavlyaem id pol'zovatelya , kotorıy hoçet podpisatsiya b cpisok id podpicannih pol'zovatelya /



    #dobavlyaem id pol'zovatelya , kotorıy hoçet podpisatsiya b cpisok id podpicannih pol'zovatelya / 
    #add the id of the user who wants to subscribe to the list of subscribed users

    return JsonResponse({
        "success": True,
        "message": f"You have successfully followed {user_to_follow.username}",
    })    

def unfollow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id) 
    current_user=request.user 

    target_profile , _ = UserProfile.objects.get_or_create(user=user_to_follow) 
    
    subscriber_file , _= Subscriber.objects.get_or_create(user_profile=target_profile)

    subscriber_file.subscriber.remove(current_user) 

    return JsonResponse({
        "success": True,
        "message": f"You have successfully unfollowed {user_to_follow.username}",
    })    


