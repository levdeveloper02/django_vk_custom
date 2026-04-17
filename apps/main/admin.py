from django.contrib import admin
from .models import HomesSlider, Category, Post

# Register your models here.

#tablolarımızı yönetim paneline eklemek için için kullanılan dosya/ 
#file for registering our models to the admin panel

#yönetici panelinde bir modelin görünmesi için admin.site.register() fonksiyonu kullanılır./
#register a model to the admin panel using admin.site.register() function



class HomesSliderAdmin(admin.ModelAdmin): 
    list_display = ["id", "image"] #fields to display in the admin panel

admin.site.register(HomesSlider, HomesSliderAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "is_active" , "created_at"]
    list_display_links =["id", "name"] #list of fields that, when clicked, goto the detailed page
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["is_active"] #list of fields that can be edited on the all items page
    list_filter = ["is_active", "created_at"] #list of fields for filtering elements
    search_fields = ["name"] #list of fields for searching

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =["id", "title", "views_quantity", "author", "category"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["views_quantity"]
    list_filter=["author", "category","created_at"]
    actions =["delete_selected_posts"] 
    

    
