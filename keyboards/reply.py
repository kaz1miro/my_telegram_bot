
from telebot import types
from urllib3.util import resolve_cert_reqs


def generate_reply_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    but1 = types.KeyboardButton("Первая кнопка")
    but2 = types.KeyboardButton("Вторая кнопка")

    markup.add(but1,but2)

    return markup

