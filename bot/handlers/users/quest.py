from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.inline.quest_keyboard import quest_kb, reload_quest_kb
from bot.states.totem_quiz import TotemQuiz
from loader import dp

QUESTIONS = [
    {
        "text": "🐾 Как ты проводишь свободное время?",
        "options": {
            "На природе 🏕": "wolf",
            "С друзьями 🍻": "dog",
            "В одиночестве 📚": "owl",
        },
    },
    {
        "text": "🌙 Что тебе ближе по духу?",
        "options": {
            "Ночь и тайна 🌌": "owl",
            "Свобода и охота 🐺": "wolf",
            "Верность и тепло 🐶": "dog",
        },
    },
    {
        "text": "🔥 Как ты реагируешь на трудности?",
        "options": {
            "Спокойно и мудро 🦉": "owl",
            "Беру всё под контроль 🐺": "wolf",
            "Надеюсь на поддержку 💛": "dog",
        },
    },
]

RESULTS = {
    "wolf": "🐺 <b>Твой тотем — Волк!</b>\nСимвол силы, свободы и верности стае.",
    "dog": "🐶 <b>Твой тотем — Собака!</b>\nТы добр, предан и всегда рядом с близкими.",
    "owl": "🦉 <b>Твой тотем — Сова!</b>\nТы мудр, наблюдателен и любишь уединение.",
}


async def send_question(message: types.Message, index: int):
    q = QUESTIONS[index]
    markup = InlineKeyboardMarkup()
    for text, value in q["options"].items():
        markup.add(InlineKeyboardButton(text, callback_data=f"answer_{value}_{index}"))
    await message.edit_text(q["text"], reply_markup=markup)


@dp.callback_query_handler(Text(equals='quest'), state='*')
async def quest_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer(' ')
    await state.reset_state(True)

    await call.message.edit_text('''🔥 <b>Пришло время для мини-квеста!</b>

Ответь на три вопроса и узнай — какое твое тотемное животное!

👇Чтобы начать, нажми на соответствующую кнопку''', reply_markup=quest_kb())


@dp.callback_query_handler(Text(equals='start_quest'), state='*')
async def start_quest_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer(' ')
    await state.update_data(answers=[])
    await send_question(call.message, 0)
    await TotemQuiz.first_question.set()


@dp.callback_query_handler(Text(startswith="ans_"), state=TotemQuiz.all_states)
async def handle_answer(call: types.CallbackQuery, state: FSMContext):
    _, animal, index = call.data.split("_")
    index = int(index)

    data = await state.get_data()
    answers = data.get("answers", [])
    answers.append(animal)
    await state.update_data(answers=answers)

    await call.answer("✅ Ответ принят")

    if index < len(QUESTIONS) - 1:
        await send_question(call.message, index + 1)
        await TotemQuiz.next()
    else:
        result = max(set(answers), key=answers.count)
        await state.finish()
        await call.message.edit_text(RESULTS[result], reply_markup=reload_quest_kb())
