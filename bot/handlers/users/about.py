from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.keyboards.inline.go_to_menu_keyboard import go_menu_kb
from loader import dp


@dp.callback_query_handler(Text(equals='about'), state='*')
async def about_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer(' ')
    await state.reset_state(True)

    await call.message.edit_text('''<b>ℹ️ О боте</b>
    
• Основные функции:
<blockquote><b>🎯 Пройти квест</b>
Я задам тебе 3 вопроса и помогу понять какое твое тотемное животное

<b>🤖 Получить совет от ИИ</b>
Не можешь разобраться в чем-то? Задай вопрос и тут же получи ответ!

<b>ℹ️ О боте</b>
Сейчас ты тут, краткая информация о моих возможностях</blockquote>

• Команды:

/start — Запустить бота
/get_questions — Получить все ответы из формы мини-приложения

ℹ️ Если у тебя возникли проблемы с ботом или где-то нашел ошибку, напиши в поддержку, нажав <a href="https://t.me/bichief">сюда</a>''',
                                 reply_markup=go_menu_kb())
