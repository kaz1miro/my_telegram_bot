def get_username_or_id(message):
    if message.from_user.username is not None:
        return f"@{message.from_user.username}"
    else:
        return f"Пользователь с ID {message.from_user.id} (без username)"
