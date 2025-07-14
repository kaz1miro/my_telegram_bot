import utilities as util

import telebot

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    try:

        bot.send_message(
            chat_id=message.chat.id,
            text= f"Привет, {message.from_user.first_name} я новый телеграм бот"
        )
        bot.send_message(
            chat_id= config.MY_CHAT_ID,
            text= f" {util.get_username_or_id(message)} запустил бота"
        )
    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Произошла ошибка, попробуйте написать позже"
        )
        print(f"Произошла непредвиденная ошибка: {e}")

@bot.message_handler(commands=['button'])

@bot.message_handler(content_types=['text'])
def text_handler(message):
    try:
        if message.text.startswith('/'):
            return
        bot.send_message(
            chat_id= message.chat.id,
            text=f"Вы написали: {message.text}"
        )

        bot.send_message(
            chat_id=config.MY_CHAT_ID,
            text=f"Мне написал {util.get_username_or_id(message)} Текст сообщения:  {message.text} "
        )


    except Exception as e:
        print(f"Ошибка при обработке сообщения, подробнее: {e}")

@bot.message_handler(content_types=['audio'])
def audio_handler(message):
    try:
        bot.send_message(
            message.chat.id,
            f"Вы прислали аудиофайл"
        )
        bot.send_message(
            chat_id=config.MY_CHAT_ID,
            text=f"Пользователь {util.get_username_or_id(message)}, прислал аудиофайл"
        )

    except Exception as e:
        print(f"Произошла ошибка при обработке аудиофайла, ошибка: {e}")

@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    try:
        bot.send_message(
            message.chat.id,
            f'Вы прислали фото'
        )
        bot.send_message(
            chat_id=config.MY_CHAT_ID,
            text=f"Пользователь {util.get_username_or_id(message)}, прислал фото"
        )
        photo_id = message.photo[-1].file_id
        bot.send_photo(config.MY_CHAT_ID, photo_id)
    except Exception as e:
        print(f"Ошибка при обработке фото: {e}")


@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    try:
        bot.send_message(
            message.chat.id,
            f'Вы прислали голосовое сообщение')

        bot.send_message(
            chat_id=config.MY_CHAT_ID,
            text=f"Пользователь {util.get_username_or_id(message)}, прислал голосовое сообщение"
        )
    except Exception as e:
        print(f"При обработке голосового сообщения произошла ошибка: {e}")


bot.polling(none_stop=True, interval=0)