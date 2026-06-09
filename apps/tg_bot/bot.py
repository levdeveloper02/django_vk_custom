from core.settings import BOT_TOKEN
from telebot import TeleBot, types
from django.contrib.auth.models import User
from .models import TelegramBotUser

bot = TeleBot(token=BOT_TOKEN)



@bot.message_handler(commands=['start'])
def handler_start(message):
    print(f" gelen mesaj: {message.text}")


    chat_id=message.chat.id

    parts= message.text.split()

    if len(parts) < 2: # EĞER sadece /start yazdıysa (peşinde ID yoksa) çökmeyi engelle!
        bot.send_message(chat_id,"Lütfen web sitesindeki onay linkine tıklayarak bota giriş yapın!")
        return 

    user_id=parts[1] #Eğer 2 parçaysa (yani /start 17 gibiyse) güvenle ID'yi alırız

    TelegramBotUser.objects.update_or_create(
        tg_chat_id=chat_id,
        defaults={
            'user_id': int(user_id),
            'tg_username': message.chat.username
        }   
    )
    bot.send_message(chat_id,"Bot'a hoş geldiniz! Artık bildirimleri alacaksınız.")
    bot.send_message(chat_id, "<a href='http://127.0.0.1:8000/users/login/'> voyti v akkaunt </a>", parse_mode='HTML')

    if __name__ == "__main__":
        print("Bot is running...")
        bot.infinity_polling()
        print("Bot stopped.")


