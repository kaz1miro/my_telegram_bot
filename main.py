import telebot

import config
from handlers import *

bot = telebot.TeleBot(config.TOKEN)

register_commands_handlers(bot)
register_text_handlers(bot)
register_media_handlers(bot)
register_callbacks_handlers(bot)




if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True, interval=0)