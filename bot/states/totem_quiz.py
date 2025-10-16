from aiogram.dispatcher.filters.state import StatesGroup, State


class TotemQuiz(StatesGroup):
    first_question = State()
    second_question = State()
    third_question = State()
