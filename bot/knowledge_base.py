# knowledge_base.py

import os
import time
import threading
from bot.search_engine import index_documents, load_links
from bot.config import UPDATE_INTERVAL_HOURS

class KnowledgeBase:
    """ Класс для управления базой знаний и её регулярного обновления. """
    
    def __init__(self):
        self.links = load_links()
        self.indexed_docs = index_documents(self.links)
        self.start_auto_update()

    def update_knowledge(self):
        """ Обновляет базу знаний, загружая свежие документы. """
        print("🔄 Обновление базы знаний...")
        self.links = load_links()
        self.indexed_docs = index_documents(self.links)
        print(f"✅ База знаний обновлена: {len(self.indexed_docs)} документов.")

    def start_auto_update(self):
        """ Запускает автоматическое обновление в фоновом потоке. """
        def updater():
            while True:
                time.sleep(UPDATE_INTERVAL_HOURS * 3600)  # Перевод часов в секунды
                self.update_knowledge()

        threading.Thread(target=updater, daemon=True).start()

    def search(self, query):
        """ Ищет информацию в базе знаний. """
        from bot.search_engine import search_query
        return search_query(query, self.indexed_docs)

# Создаём единственный экземпляр базы знаний
knowledge_base = KnowledgeBase()
