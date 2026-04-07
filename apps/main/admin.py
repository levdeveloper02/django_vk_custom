from django.contrib import admin
from .models import HomesSlider

# Register your models here.

#tablolarımızı yönetim paneline eklemek için için kullanılan dosya/ 
#file for registering our models to the admin panel

#yönetici panelinde bir modelin görünmesi için admin.site.register() fonksiyonu kullanılır./
#register a model to the admin panel using admin.site.register() function


class HomesSliderAdmin(admin.ModelAdmin): 
    list_display = ["id", "image"] #fields to display in the admin panel

admin.site.register(HomesSlider, HomesSliderAdmin)