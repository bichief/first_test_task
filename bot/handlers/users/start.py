from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text

from bot.keyboards.inline.main_menu_keyboard import main_menu_kb
from bot.utils.db_api.db_commands import create_user
from loader import dp


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    await create_user(
        name=message.from_user.first_name,
        username=message.from_user.username,
        telegram_id=message.from_user.id,
    )

    await message.answer(f'''<b>🖐️ Привет, {message.from_user.first_name}!</b>

Ты можешь воспользоваться моим функционалом, нажав на кнопки ниже:''', reply_markup=main_menu_kb())


@dp.callback_query_handler(Text(equals='go_menu'), state='*')
async def go_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer(' ')
    await state.reset_state(True)
    await call.message.edit_text(f'''<b>🖐️ Привет, {call.from_user.first_name}!</b>

Ты можешь воспользоваться моим функционалом, нажав на кнопки ниже:''', reply_markup=main_menu_kb())
