from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def go_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='go_menu')
        ]
    ])
