# handlers.py

from aiogram import types, Dispatcher
from bot.utils import normalize_text, is_wrong_layout

WELCOME_MSG = (
    "Привет, я Тенгри 🤖\n"
    "Я постараюсь помочь тебе с вопросами по документации.\n"
    "Я еще учусь, так что если вдруг скажу чушь — не суди строго 😉"
)

async def start_cmd(msg: types.Message):
    await msg.answer(WELCOME_MSG)

async def handle_message(msg: types.Message):
    text = msg.text
    if is_wrong_layout(text):
        await msg.reply("Кажется, у тебя раскладка не та 🙃 Попробуй переключить и повторить.")
        return

    norm_text = normalize_text(text)
    # Здесь будет вызов поиска по embedding'ам и документам
    await msg.answer(f"Пока что я просто повторю твой вопрос: '{norm_text}' 🧠")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
    dp.register_message_handler(handle_message)