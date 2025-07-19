import config
import utilities as util



def register_media_handlers(bot):
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
