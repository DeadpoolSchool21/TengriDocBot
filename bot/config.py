# config.py

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Токены для работы бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
GIGACHAT_TOKEN = os.getenv("GIGACHAT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в .env файле")

if not GIGACHAT_TOKEN:
    print("⚠️ GigaChat токен отсутствует, но бот может работать без него.")

# Идентификаторы администраторов (можно расширять)
ADMIN_IDS = ["@petr_yx_a"]

# Настройки обновления базы знаний
UPDATE_INTERVAL_HOURS = 24  # Раз в сутки
DOCUMENTS_PATH = "data/docs_links.txt"

# Параметры логирования
LOG_FILE = "bot.log"
LOG_LEVEL = "INFO"
