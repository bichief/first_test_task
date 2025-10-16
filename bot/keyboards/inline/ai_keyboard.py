from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ai_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔁 Задать еще вопрос', callback_data='ai_answer')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='go_menu')
        ]
    ])
