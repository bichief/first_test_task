from aiogram.dispatcher.filters.state import StatesGroup, State


class AiQuestion(StatesGroup):
    question = State()
