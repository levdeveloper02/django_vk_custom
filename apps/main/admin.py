from django.contrib import admin
from .models import HomesSlider, Category, Post, PostComment, PostImage, FAQ

# Register your models here.

# tablolarımızı yönetim paneline eklemek için için kullanılan dosya/
# file for registering our models to the admin panel

# yönetici panelinde bir modelin görünmesi için admin.site.register() fonksiyonu kullanılır./
# register a model to the admin panel using admin.site.register() function


class HomesSliderAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]  # fields to display in the admin panel


admin.site.register(HomesSlider, HomesSliderAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "is_active", "created_at"]
    # list of fields that, when clicked, goto the detailed page
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}
    # list of fields that can be edited on the all items page
    list_editable = ["is_active"]
    # list of fields for filtering elements
    list_filter = ["is_active", "created_at"]
    search_fields = ["name"]  # list of fields for searching


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # number of extra forms to display

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "views_quantity", "author", "category"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["views_quantity"]
    list_filter = ["author", "category", "created_at"]
    actions = ["delete_selected_posts"]
    inlines = [PostImageInline]
     
    @admin.action(description="Delete selected posts")
    def delete_selected_posts(self, queryset):
        queryset.delete() 


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "show_content", "post", "created_at"]
    list_filter = ["user", "post", "updated_at"]
    search_fields = ["content"]
    
    
    @admin.display(description="kommentariy")  # set the column name in the admin panel
    def show_content(self, obj):
        return obj.content[:60]
    


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass
