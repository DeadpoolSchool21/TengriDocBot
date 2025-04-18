# TengriDocBot  

## 📌 Описание проекта  
**TengriDocBot** — это интеллектуальный помощник, который ежедневно загружает документацию, анализирует её и предоставляет точные ответы пользователям.  
Бот интегрирован в **Telegram**, а также может быть адаптирован для **СберЧата** и работы на **Linux (Debian) и macOS**.  

### ⚡ Основные возможности  
✔ Автоматическая загрузка документов и их индексирование  
✔ Семантический поиск по документации  
✔ Интеграция с GigaChat (автоматическое получение токена)  
✔ Запоминание последних 10 сообщений  
✔ Исправление раскладки и опечаток  
✔ Эмоциональность и чувство юмора  

---

## 📂 Структура проекта  

```
TengriDocBot/
│── bot/
│   ├── __init__.py            # Инициализация пакета  
│   ├── config.py              # Конфигурационный файл (токены, переменные окружения)  
│   ├── gigachat_client.py     # Интеграция с GigaChat (автополучение токена)  
│   ├── search_engine.py       # Загрузка и поиск информации в документации  
│   ├── knowledge_base.py      # Автоматическое обновление базы знаний (без крона)  
│   ├── handlers.py            # Основная обработка сообщений  
│   ├── utils.py               # Исправление раскладки и нормализация текста  
│   ├── memory.py              # Запоминание последних 10 сообщений  
│   ├── humor.py               # Юмор и эмоциональность бота  
│   ├── main.py                # Запуск бота  
│── data/
│   ├── docs_links.txt         # Список ссылок на документацию  
│   ├── history.json           # Хранение истории диалогов  
│── requirements.txt           # Список зависимостей  
│── install_requirements.py    # Скрипт для установки необходимых библиотек  
│── get_gigachat_token.py      # Запрос и получение токена GigaChat  
│── README.md                  # Описание проекта  
```

---

## 📝 Описание файлов  

**🔹 `config.py`** — конфигурация бота (токены, настройки).  
**🔹 `gigachat_client.py`** — подключение к GigaChat, автополучение токена.  
**🔹 `search_engine.py`** — загрузка документации и семантический поиск.  
**🔹 `knowledge_base.py`** — автоматическое обновление базы знаний.  
**🔹 `handlers.py`** — обработка сообщений и взаимодействие с пользователем.  
**🔹 `utils.py`** — исправление раскладки и опечаток.  
**🔹 `memory.py`** — хранение последних 10 сообщений для контекста.  
**🔹 `humor.py`** — добавляет эмоциональность и чувство юмора.  
**🔹 `main.py`** — запуск бота и управление диспетчером.  
**🔹 `install_requirements.py`** — установка зависимостей.  
**🔹 `get_gigachat_token.py`** — получение токена GigaChat через OAuth.  

---

## 🚀 Установка и запуск  

### 1️⃣ Установка зависимостей  
Перед запуском установите необходимые библиотеки:  
```bash
python install_requirements.py
```

### 2️⃣ Получение токена GigaChat  
Бот автоматически получает токен через `get_gigachat_token.py`.  

### 3️⃣ Запуск бота  
Запустите основную программу:  
```bash
PYTHONPATH=$(pwd) python bot/main.py
```

💡 **Бот начнёт работать, загружая документацию и отвечая на вопросы!** 🎉  

---

### 🛠 Дальнейшие улучшения  
- 🔄 Расширение базы знаний  
- 🤖 Интеграция с СберЧатом  
- 📊 Улучшение логики анализа документации  


## Запуск
```bash
pip install -r requirements.txt
python bot/main.py
```

## Настройка
В `config.py` вставьте свой Telegram Bot Token и список ID админов.

## Автор
@petr_yx_a 💚

## Проверка установленных библиотек
```bash
python install_requirements.py
```

## Запуск бота
```bash
PYTHONPATH=$(pwd) python bot/main.py
```