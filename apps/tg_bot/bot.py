from core.settings import BOT_TOKEN
from telebot import TeleBot, types
from django.contrib.auth.models import User
from .models import TelegramBotUser

bot = TeleBot(token=BOT_TOKEN)



@bot.message_handler(commands=['start'])
def handler_start(message):
    print(message.text)


    chat_id=message.chat.id



    _, user_id= message.text.split() # /start 123
    # print(user_id)
    TelegramBotUser.objects.create(
        user_id=int(user_id),
        tg_username=message.chat.username,
        tg_chat_id=chat_id
        
    )
    bot.send_message(chat_id, "vıy ucpeshno zaregistrirovany v botu")

    bot.send_message(chat_id, "<a href='http://127.0.0.1:8000/users/login/' > voyti v akkaunt </a>",
                     parse_mode='HTML')


