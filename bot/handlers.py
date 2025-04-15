# handlers.py

from aiogram import Router, types
from bot.search_engine import search_query
from bot.gigachat_client import gigachat_client  # Исправленный импорт!
from bot.memory import conversation_memory
from bot.utils import normalize_text, is_wrong_layout
from bot.humor import get_greeting, get_bot_abilities, get_joke
from bot.get_gigachat_token import gigachat_auth  # Импортируем токен GigaChat

router = Router()
indexed_docs = []

def register_handlers(dp, docs):
    """ Регистрация обработчиков и загрузка базы знаний. """
    global indexed_docs
    indexed_docs = docs
    dp.include_router(router)

@router.message()
async def handle_message(message: types.Message):
    """ Основная логика обработки сообщений от пользователя. """
    user_text = message.text.strip()

    # Проверка раскладки клавиатуры
    if is_wrong_layout(user_text):
        await message.answer("🔄 Похоже, ты забыл сменить раскладку. Попробуй снова!")
        return

    # Нормализация текста
    normalized_text = normalize_text(user_text)

    # Проверка на приветствие
    if normalized_text in ["привет", "здравствуй", "хай", "добрый день"]:
        await message.answer(get_greeting())
        return

    # Проверка на запрос "Что ты умеешь?"
    if "что ты умеешь" in normalized_text:
        await message.answer(get_bot_abilities())
        return

    # Запоминаем диалог
    conversation_memory.add_message(user_text, "⏳ Думаю над ответом...")

    # Проверка наличия токена GigaChat
    if not gigachat_auth.access_token:
        gigachat_auth.access_token = gigachat_auth.get_gigachat_token()
        print(f"🔄 Новый токен GigaChat в handlers.py: {gigachat_auth.access_token}")

    # Поиск в базе знаний
    search_results = search_query(normalized_text, indexed_docs)
    
    if search_results:
        response_text = "\n\n---\n\n".join([f"{doc[2]}\nИсточник: {doc[1]}" for doc in search_results])
        full_prompt = f"Вот фрагменты из документации:\n{response_text}\n\nВопрос: {user_text}\nОтветь понятно и коротко."
        
        # Запрашиваем ответ у GigaChat (если доступен)
        try:
            reply = gigachat_client.ask_gigachat(full_prompt)  # Исправленный вызов!
            conversation_memory.add_message(user_text, reply)
            await message.answer(f"🧠 {reply}")
        except Exception as e:
            await message.answer("🚨 Ошибка при обращении к GigaChat. Использую локальные данные.")
            print(f"GigaChat Error: {e}")
            await message.answer(response_text)
    else:
        await message.answer("😕 Не нашёл точного ответа в документации. Могу попробовать сформулировать общий ответ?")
