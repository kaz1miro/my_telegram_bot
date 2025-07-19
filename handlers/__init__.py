from .commands import register_commands_handlers
from .callbacks import register_callbacks_handlers
from .text import register_text_handlers
from .media import register_media_handlers




__all__ = [
    'register_commands_handlers',
    'register_media_handlers',
    'register_text_handlers',
    'register_callbacks_handlers'
    ]