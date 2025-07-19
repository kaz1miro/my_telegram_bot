








def register_callbacks_handlers(bot):
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
