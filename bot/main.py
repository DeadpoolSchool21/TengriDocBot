# main.py

from aiogram import Bot, Dispatcher, executor, types
from bot.config import BOT_TOKEN
from bot.handlers import register_handlers
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    print("TengriDocBot запущен 🚀")
    executor.start_polling(dp, skip_updates=True)