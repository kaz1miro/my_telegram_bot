import config
from telebot import  types
import utilities as util


def register_text_handlers(bot):
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
                chat_id=message.chat.id,
                text=f"Вы написали: {message.text}"
            )

            bot.send_message(
                chat_id=config.MY_CHAT_ID,
                text=f"Мне написал {util.get_username_or_id(message)} Текст сообщения:  {message.text} "
            )


        except Exception as e:
            print(f"Ошибка при обработке сообщения, подробнее: {e}")

