from textwrap import dedent
from keyboards import *
import config
from telebot import types





def register_commands_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        try:

            bot.send_message(
                chat_id=message.chat.id,
                text=f"Привет, {message.from_user.first_name} я новый телеграм бот"
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


            bot.send_message(
                chat_id=message.chat.id,
                text="Добавились кнопки inline",
                reply_markup=generate_inline_buttons()

            )
            bot.send_message(
                chat_id=message.chat.id,
                text="Добавились кнопки reply",
                reply_markup=generate_reply_buttons()

            )

        except Exception as e:
            bot.send_message(
                chat_id=message.chat.id,
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


