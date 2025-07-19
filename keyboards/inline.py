from telebot import types

def generate_inline_buttons():
    inline_markup = types.InlineKeyboardMarkup(row_width=2)

    btn_yes = types.InlineKeyboardButton("Да", callback_data="answer_yes")
    btn_no = types.InlineKeyboardButton("Нет", callback_data="answer_no")

    inline_markup.add(btn_yes, btn_no)
    return inline_markup