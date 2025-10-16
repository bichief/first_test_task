import aiohttp

from bot.data.config import OPENAI_API_KEY


async def ask_chatgpt(question: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Ты — помощник Telegram-бота. "
                    "Отвечай кратко и красиво, используя HTML-разметку "
                    "(<b>, <i>, <u>, <code>, <a> и т.д.) для форматирования текста."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status != 200:
                error = await response.text()
                raise Exception(f"OpenAI API error {response.status}: {error}")

            data = await response.json()
            return data["choices"][0]["message"]["content"]
