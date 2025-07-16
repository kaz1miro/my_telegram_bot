import utilities as util
from textwrap import dedent
import telebot
from telebot import types

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
            chat_id=config.MY_CHAT_ID,
            text=dedent(f"""
                Новый пользователь запустил бота
                Полная информация о пользователе:
                id: {message.from_user.id}
                username: {message.from_user.username}
                firstname: {message.from_user.first_name}
                lastname: {message.from_user.last_name}
                is bot: {message.from_user.is_bot}
                language_code: {message.from_user.language_code}
                is_premium: {message.from_user.is_premium}
            """)
        )

    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Произошла ошибка, попробуйте написать позже"
        )
        print(f"Произошла непредвиденная ошибка: {e}")

@bot.message_handler(commands=['button'])
def button(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        but1 = types.KeyboardButton("Первая кнопка")
        but2 = types.KeyboardButton("Вторая кнопка")

        markup.add(but1,but2)
        bot.send_message(
            chat_id=message.chat.id,
            text = "Добавились кнопки",
            reply_markup=markup

        )

        inline_markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton("Да", callback_data="answer_yes")
        btn_no = types.InlineKeyboardButton("Нет", callback_data="answer_no")
        inline_markup.add(btn_yes,btn_no)
        bot.send_message(
            chat_id=message.chat.id,
            text="Добавились кнопки inline",
            reply_markup=inline_markup

        )

    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Произошла ошибка, попробуйте написать позже"
        )
        print(f"Произошла непредвиденная ошибка: {e}")

# Обработчик нажатий на Inline-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'answer_yes':
                bot.answer_callback_query(call.id, "Вы выбрали 'Да'!")
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text="Отлично! Вот ваш ответ.",
                    reply_markup=None
                )

            elif call.data == 'answer_no':
                bot.answer_callback_query(call.id, "Вы выбрали 'Нет'!")
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text="Жаль, что вы отказались.",
                    reply_markup=None
                )

    except Exception as e:
        bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Произошла ошибка, попробуйте написать позже"
        )
        print(f"Произошла непредвиденная ошибка: {e}")


@bot.message_handler(commands=['hide'])
def hide_buttons(message):
    try:
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Убираю кнопки...", reply_markup=markup)

    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Произошла ошибка, попробуйте написать позже"
        )
        print(f"Произошла непредвиденная ошибка: {e}")
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