from django.db import models

class TelegramBotUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, verbose_name="polzovatel")
    tg_username=models.CharField(max_length=100, unique=True, verbose_name="imya polzovatelya v tg")
    tg_chat_id=models.BigIntegerField(unique=True, verbose_name="ID polzovatelya v tg")

    def __str__(self):
        return f"{self.user.first_name}:{self.tg_username}: {self.tg_chat_id} "
    

    class Meta:
        verbose_name="Akkauat polzovatelya v tg"
        verbose_name_plural=" akkaunt' polzavateley v tg"

        