import uuid
from django.db import models
from django.urls import reverse

"""
create table if not exists categoires(
id integer primary key autoincrement,
name varchar(255) not null unique...);
"""

# ORM

# main_homeslider - main application (app) - main/models.py


class HomesSlider(models.Model):
    id = models.UUIDField(editable=False, primary_key=True,
                          default=uuid.uuid4)  # primary key for the model
    # media/slider/image_name.png | verbose_name="foto" - a name for the field in the admin panel
    image = models.ImageField(upload_to="home/slider/", verbose_name="foto")

    def __str__(self):  # string representation of the model - how the model will be displayed in the admin panel
        return f"Fotka c ID:{self.id}"

    class Meta:
        # ilk tablo(tekil) adı / a table name in singular form
        verbose_name = "foto claydera"
        # ikinci tablo(çoğul) adı / a table name in plural form
        verbose_name_plural = "fotki claydera"


# abctraktanya model'

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Data cozdaniya", auto_now_add="True")  # 2026-04-09 15:10
    updated_at = models.DateField(
        verbose_name="Data izmeneniya", auto_now_add="True")

    class Meta:
        abstract = True  # makes it so that this model is not added to the database / abstract model

# Category object(1)
# Category object(2)
# Category object(3)


class Category(BaseModel):
    # varchar(100) not null unique
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Nazvaniye")
    # slug - a string that can be used in URLs, unique - each category must have a unique slug
    slug = models.SlugField(max_length=120, unique=True,
                            verbose_name="Korotkaya cc'lka")
    # boolean field to indicate if the category is active or not
    is_active = models.BooleanField(default=True, verbose_name="Aktivna")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kategoriya"
        verbose_name_plural = "Kategorii"


class Post(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name="nazvaniye", unique=True)
    slug = models.SlugField(max_length=140, verbose_name="Slag", unique=True)
    short_description = models.TextField(verbose_name="Kratkoe opisaniye")
    full_description = models.TextField(
        verbose_name="polnoye opisaniye", null=True, blank=True)
    # media/posts/%Y/%m/%d  2026/04/09
    preview = models.ImageField(
        upload_to="media/previews/%y/%m/%d", verbose_name="prev'iyu")
    views_quantity = models.IntegerField(
        default=0, verbose_name="Kol-vo prosmotrov")
    is_active = models.BooleanField(default=True, verbose_name="Aktivna")
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="pol'zovatel'")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Kategoriya")

    # metod dilya poluceniya cc'lki na detal'nuyu stranitsu / method for getting the URL to the detail page
    def get_absolute_url(self):
        # reverse - a function that takes the name of a URL pattern and returns the URL, kwargs - a dictionary of keyword arguments to pass to the URL pattern
        return reverse("news-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "Posts"


"""
user_id İNTEGER,
FOREİGN KEY(user_id) REFERENCES users(id)
"""


"""
cozdat' tablitsa PostComment / create a table PostComment (homework)
user
post
content
created_at
updated_at

"""


class PostComment(BaseModel):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="pol'zovatel'",
                             related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="post",
                             related_name="statiya")
    content = models.TextField(verbose_name="kommentariy")
    created_at = models.DateTimeField(
        verbose_name="data sozdaniya", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="data izmeneniya", auto_now=True)

    def __str__(self):
        return f"Kommentariy dlya {self.post.title}' ot '{self.user.username}"
    

    class Meta:
        verbose_name = "kommentariy posta"
        verbose_name_plural = "Kommentarii postov"

def make_post_image_path(instance:"PostImage", filename:str):
    return f"media/images/{instance.post.slug}/{filename}"

class PostImage(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="post",
                             related_name="images")
    image = models.ImageField(upload_to=make_post_image_path, verbose_name="foto")

    class Meta:
        verbose_name = "foto post"
        verbose_name_plural = "foto posts"


# auth.User = PostComment.objects.filter(user=user) - filter comments by user 
#related_name="comments" = user.comments.all() - default related name for reverse relation
# user.postcomment_set.all() - default related name for reverse relation


# id
# name
# slug


# b mire


# categories/1
# categories/category-name
