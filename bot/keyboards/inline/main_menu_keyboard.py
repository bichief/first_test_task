from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🎯 Пройти квест', callback_data='quest')
        ],
        [
            InlineKeyboardButton(text='🤖 Получить совет от ИИ', callback_data='ai_answer')
        ],
        [
            InlineKeyboardButton(text='ℹ️ О боте', callback_data='about')
        ]
    ])
