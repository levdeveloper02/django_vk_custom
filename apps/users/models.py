from django.db import models

class UserProfile(models.Model): # request.user.profile.
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="users/profiles/%Y/%m/%d/", null=True)