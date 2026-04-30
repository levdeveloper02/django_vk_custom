from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import HomesSlider,Category,Post, PostComment

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
    # posts=Post.objects.all().values("title", "short_description", "preview") #select * from main_posts (error)
    posts=Post.objects.all()

    # print(request.__dict__)


    context={
        "categories_data": categories_data,
        "posts":posts
    }
    return render(request, "main/news.html", context)

#http://127.0.0.1:8000/news/categories/10

def show_by_category(request, category_slug):
    categories_data= Category.objects.all() #select * from main_categories;

    # print(request.__dict__)
    # print(request.resolver_match)
    # print(request.resolver_match.kwargs.get("category_slug")) #get the value of category_slug from the URL

    #you can get an error if: 1)more than 1 value is recieved 2)no value is received
    category=Category.objects.get(slug=category_slug) # select * from main_categories where slug = ? 

    posts = Post.objects.filter(category=category) #select * from main_posts where category_id = ?  .filter() - used for filtering data based on certain conditions, it returns a new QuerySet containing the objects that match the given criteria.
    #.filter() 
    
    context={
        "categories_data": categories_data,
        "category": category,
        "posts":posts
    }
    return render(request, "main/news.html", context)


#TODO: show post by id and slug
#news/
#news/categories/<slug>
#news/<slug>


from django.shortcuts import get_object_or_404

def show_post_detail_page(request,slug):
    # post=Post.objects.get(slug=slug) #select * from main_posts where slug = ? 
    post=get_object_or_404(Post, slug=slug) #select * from main_posts where slug = ?  if no object is found, it raises a 404 error instead of throwing an exception
    if request.method == "POST":
        comment_text=request.POST.get("post_comment") #get the value of post_comment from the form data
        print(request.POST)
        if comment_text and request.user.is_authenticated:
            comment = PostComment.objects.create(
            user=request.user,
            post=post,
        content=request.POST.get("post_comment")
        )
        comment.save()
        return redirect("news-detail", slug=slug) #redirect to the same page after submitting the comment
    
    # comments= PostComment.objects.filter(post=post) #select * from main_postcomment where post_id = ?
    context={
        "post": post
    }

    return render(request, "main/news_detail.html", context)

def show_login_page(request):
    return render(request, "main/login.html")



