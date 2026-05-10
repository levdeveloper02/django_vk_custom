from slugify import slugify
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import HomesSlider, Category, Post, PostComment, UserPostView, PostLike, PostDislike
from .forms import PostForm
from django.views.generic import UpdateView


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "main/news_create.html"
    slug_url_kwarg = "slug"

# Create your views here.

# https://127.0.1:8000/main
# hello world

# select * from main_homesslider;


def render_home_main(request):
    # return HttpResponse("Hello world!!!")
    slider_photos = HomesSlider.objects.all()  # select * from main_homesslider;
    context = {
        "slider_photos": slider_photos
    }
    return render(request, "main/index.html", context=context)


def show_about_page(request):
    return render(request, "main/about.html")


def show_faq_page(request):
    return render(request, "main/faq.html")


categories_data = ["Sports", "Politics", "World", "Space", "Science"]


def show_news_page(request):
    categories_data = Category.objects.all()  # select * from main_categories;
    # posts=Post.objects.all().values("title", "short_description", "preview") #select * from main_posts (error)
    posts = Post.objects.all()

    # print(request.__dict__)

    context = {
        "categories_data": categories_data,
        "posts": posts
    }
    return render(request, "main/news.html", context)

# http://127.0.0.1:8000/news/categories/10


def show_by_category(request, category_slug):
    categories_data = Category.objects.all()  # select * from main_categories;

    # print(request.__dict__)
    # print(request.resolver_match)
    # print(request.resolver_match.kwargs.get("category_slug")) #get the value of category_slug from the URL

    # you can get an error if: 1)more than 1 value is recieved 2)no value is received
    # select * from main_categories where slug = ?
    category = Category.objects.get(slug=category_slug)

    # select * from main_posts where category_id = ?  .filter() - used for filtering data based on certain conditions, it returns a new QuerySet containing the objects that match the given criteria.
    posts = Post.objects.filter(category=category)
    # .filter()

    context = {
        "categories_data": categories_data,
        "category": category,
        "posts": posts
    }
    return render(request, "main/news.html", context)


# TODO: show post by id and slug
# news/<int:id>-<slug:slug>
# news/categories/<slug>
# news/<slug>


def show_post_detail_page(request, slug):
    # post=Post.objects.get(slug=slug) #select * from main_posts where slug = ?
    # select * from main_posts where slug = ?  if no object is found, it raises a 404 error instead of throwing an exception
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        comment_text = request.POST.get("post_comment")
        if comment_text and request.user.is_authenticated:
            comment = PostComment.objects.create(
                user=request.user,
                post=post,
                content=comment_text
            )
        return redirect("news-detail", slug=slug)

    if request.user.is_authenticated:
        post_view, post_views_created = UserPostView.objects.get_or_create(
            user=request.user,
            post=post
        )  # select * from main_userpostview where user_id =? and post_id=?
        if post_views_created:
            post.views_quantity += 1
            post.save()

    context = {
        "post": post
    }
    return render(request, "main/news_detail.html", context)


def show_login_page(request):
    return render(request, "main/login.html")


def create_post(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news_form = form.save(commit=False)  # do not write to the database

            news_form.author = request.user  # set the author of the post to the current user
            # generate a slug from the title of the post
            news_form.slug = slugify(news_form.title)
            news_form.save()  # save the form to the database
            # redirect to the news page after creating a post
            return redirect("news-detail", news_form.slug)
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, "main/news_create.html", context)


def add_like_or_dislike(request, post_slug, action):
    # Kullanıcı giriş yapmamışsa işlem yapmasına izin verme (Bonus güvenlik!)
    if not request.user.is_authenticated:
        return redirect("login")  # Veya kendi giriş sayfanın adı neyse

    post = get_object_or_404(Post, slug=post_slug)

    post_like_obj, _ = PostLike.objects.get_or_create(post=post)
    post_dislike_obj, _ = PostDislike.objects.get_or_create(post=post)

    # HTML'den gelen parolayı "add_like" olarak güncelledik!
    if action == "add_like":
        if request.user not in post_like_obj.user.all():
            post_like_obj.user.add(request.user)      # Beğenenlere ekle
            post_dislike_obj.user.remove(request.user)  # Varsa dislike'tan sil
        else:
            # Zaten beğenmişse geri al
            post_like_obj.user.remove(request.user)

    elif action == "add_dislike":
        if request.user not in post_dislike_obj.user.all():
            post_dislike_obj.user.add(request.user)   # Dislike'a ekle
            post_like_obj.user.remove(request.user)   # Varsa like'tan sil
        else:
            # Zaten dislike atmışsa geri al
            post_dislike_obj.user.remove(request.user) #where user_id=?

    return redirect("news-detail", slug=post_slug)

def delete_post(request, post_slug):
    post=Post.objects.get(slug=post_slug) #select * from main_posts where slug = ?

    if request.method == "POST":
        post.delete()
        return redirect("news")

    context = {
        "post": post
    }
    return render(request, "main/post_comfirm_delete.html", context)

