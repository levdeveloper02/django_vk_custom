from django.contrib import admin
from .models import Subscriber, UserProfile

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass