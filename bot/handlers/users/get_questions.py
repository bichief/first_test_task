import logging
import os
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command
from django.utils.timezone import localtime

from bot.utils.db_api.db_commands import get_all_questions
from loader import dp


@dp.message_handler(Command('get_questions'))
async def get_questions_cmd(message: types.Message):
    questions = await get_all_questions()

    if not questions:
        return await message.answer("❌ Вопросов пока нет.")

    lines = []
    for q in questions:
        created_at = localtime(q.created).strftime("%Y-%m-%d %H:%M")
        name = q.sender.name or q.sender.username or "Без имени"
        username = f"@{q.sender.username}" if q.sender.username else ""
        lines.append(
            f"📅 {created_at}\n{name} {username} — {q.sender.telegram_id}\n❓ {q.question}\n\n"
        )

    text = "".join(lines)

    filename = f"questions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join("/tmp", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    await dp.bot.send_document(
        chat_id=message.chat.id,
        document=open(filepath, "rb"),
        caption="📄 Все вопросы пользователей"
    )
    try:
        os.remove(filepath)
    except OSError as e:
        logging.warning(f"Ошибка при удалении файла: {e}")
