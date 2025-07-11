import telebot

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет,'+ message.from_user.username +' я новый телеграм бот'
    )
    bot.send_message(
        chat_id= config.MY_CHAT_ID,
        text= "@" + message.from_user.username + " Запустил бота"
    )


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text.startswith('/'):
        return
    bot.send_message(
        message.chat.id,
        f'Вы написали: {message.text}'
    )

    bot.send_message(
        chat_id=config.MY_CHAT_ID,
        text="Мне написал @" + message.from_user.username + " Текст сообщения: " + message.text
    )

@bot.message_handler(content_types=['audio'])
def audio_chek(message):
    bot.send_message(
        message.chat.id,
        f'Вы прислали аудиофайл'
    )

@bot.message_handler(content_types=['voice'])
def voice_chek(message):
    bot.send_message(
        message.chat.id,
        f'Вы прислали голосовое сообщение')
    bot.send_message(
        chat_id=config.MY_CHAT_ID,
        text="Мне прислал голосовое @" + message.from_user.username
    )

bot.polling(none_stop=True, interval=0)