# memory.py

import json

class ConversationMemory:
    """ Управление историей диалога (запоминает последние 10 сообщений). """
    
    def __init__(self, history_path="data/history.json", max_messages=10):
        self.history_path = history_path
        self.max_messages = max_messages
        self.history = self.load_history()

    def load_history(self):
        """ Загружает историю диалога из файла. """
        try:
            with open(self.history_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_history(self):
        """ Сохраняет историю диалога в файл. """
        with open(self.history_path, "w") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def add_message(self, user_message, bot_reply):
        """ Добавляет новое сообщение в историю, удаляя старые, если их больше 10. """
        self.history.append({"user": user_message, "bot": bot_reply})
        if len(self.history) > self.max_messages:
            self.history.pop(0)  # Удаляем самое старое сообщение
        self.save_history()

    def get_recent_messages(self):
        """ Возвращает последние сообщения для контекста. """
        return self.history[-self.max_messages:]  # Последние 10 записей

# Создаём экземпляр памяти
conversation_memory = ConversationMemory()
