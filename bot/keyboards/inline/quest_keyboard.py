from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def quest_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔥 НАЧАТЬ', callback_data='start_quest'),
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='go_menu')
        ]
    ])


def reload_quest_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='🔁 Пройти еще раз', callback_data='start_quest')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='go_menu')
        ]
    ])
