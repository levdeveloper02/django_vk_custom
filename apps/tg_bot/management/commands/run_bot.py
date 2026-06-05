from django.core.management.base import BaseCommand

from apps.tg_bot.bot import bot

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Bot is running...")
        bot.infinity_polling()
        print("Bot stopped.")
        return
