from django.db import models


class UserProfile(models.Model):  # request.user.profile.
    user = models.OneToOneField(
        "auth.User", on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="users/profiles/%Y/%m/%d/", null=True)

    def __str__(self):
        return f"{self.user.username} profile"


class Subscriber(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                        related_name="subscribers",
                                        verbose_name="profil' pol'zovatelya")
    subscriber = models.ManyToManyField(
        "auth.User", related_name="subscribers", verbose_name="podpischiki")

    def __str__(self):
        # print(dir(self.subscriber))
        # return f"{self.user_profile.user.username}: {self.subscriber.count()} subscribers"
        return f"{self.user_profile.user.username}"
    

    
