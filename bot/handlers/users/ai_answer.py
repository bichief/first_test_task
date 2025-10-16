import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.keyboards.inline.ai_keyboard import ai_kb
from bot.keyboards.inline.go_to_menu_keyboard import go_menu_kb
from bot.states.ai_question import AiQuestion
from bot.utils.openai.openai_api import ask_chatgpt
from loader import dp


async def animate_thinking(chat_id, message_id):
    dots = ["", ".", "..", "..."]
    for i in range(12):
        text = f"⏳ <b>Думаю над ответом{dots[i % len(dots)]}</b>"
        await dp.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode="HTML"
        )
        await asyncio.sleep(0.5)


@dp.callback_query_handler(Text(equals='ai_answer'))
async def ai_answer_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer(' ')
    msg = await call.message.edit_text('''🤖 <b>Не можешь найти ответ на свой вопрос?</b>
Спроси ИИ!

💬 Отправь мне вопрос, а я на него отвечу''', reply_markup=go_menu_kb())
    await AiQuestion.question.set()

    await state.update_data(
        {
            'message_id': msg.message_id
        }
    )


@dp.message_handler(state=AiQuestion.question)
async def get_question_from_user_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    question = message.text
    await message.delete()

    await animate_thinking(
        chat_id=message.from_user.id,
        message_id=data['message_id']
    )

    answer = await ask_chatgpt(question)

    await dp.bot.edit_message_text(
        chat_id=message.from_user.id,
        message_id=data['message_id'],
        text=f'''✅ <b>Ответ готов!</b>

Вопрос: {question}

Ответ: {answer}

Хочешь задать еще вопрос?
👇Нажми на кнопку ниже''',
        reply_markup=ai_kb()
    )
    await state.reset_state(True)
