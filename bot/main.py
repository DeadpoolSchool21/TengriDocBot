# main.py

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode  # Исправленный импорт
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers import register_handlers
from bot.search_engine import load_links, index_documents
from bot.config import BOT_TOKEN
from bot.knowledge_base import KnowledgeBase
from bot.get_gigachat_token import gigachat_auth  # Импортируем GigaChat токен

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("bot.log", mode='w'),
        logging.StreamHandler()
    ]
)

# Проверка наличия токена бота
if not BOT_TOKEN:
    logging.error("❌ BOT_TOKEN не найден в .env файле")
    exit(1)

# Проверка наличия токена GigaChat
if not gigachat_auth.access_token or gigachat_auth.access_token == "":
    logging.warning("⚠️ Ошибка передачи токена! Принудительно запрашиваем новый...")
    gigachat_auth.access_token = gigachat_auth.get_gigachat_token()

if gigachat_auth.access_token:
    logging.info(f"✅ GigaChat токен успешно загружен: {gigachat_auth.access_token}")
else:
    logging.error("❌ Критическая ошибка: токен GigaChat не получен!")



# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)  # Исправлено!
dp = Dispatcher(storage=MemoryStorage())

async def main():
    logging.info("🤖 TengriDocBot запускается... Включаем магию!")

    try:
        # Инициализация базы знаний
        knowledge_base = KnowledgeBase()
        
        # Загрузка ссылок и документов
        links = load_links()
        logging.info(f"🔗 Загружено {len(links)} ссылок")
        
        indexed_docs = index_documents(links)
        logging.info(f"📚 Проиндексировано {len(indexed_docs)} документов")

        # Регистрация обработчиков
        register_handlers(dp, indexed_docs)
        logging.info("👌 Обработчики зарегистрированы успешно!")

        # Запуск бота
        await dp.start_polling(bot)
    
    except Exception as e:
        logging.exception(f"💥 Ошибка при запуске бота: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.exception(f"💥 Ошибка при запуске: {e}")
