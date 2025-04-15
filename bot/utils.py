# utils.py

import re
import string

# Исправленное отображение клавиатуры для корректной замены раскладки
keyboard_map = str.maketrans(
    "qwertyuiop[]asdfghjkl;'zxcvbnm,./",
    "йцукенгшщзхъфывапролджэячсмитьбю."
)

# Часто встречающиеся опечатки и исправления
TYPO_CORRECTIONS = {
    "примет": "привет",
    "здравсьте": "здравствуйте",
    "компютер": "компьютер",
    "всерда": "всегда",
    "бото": "бот",
}

def normalize_text(text):
    """ Приведение текста к нижнему регистру и удаление пунктуации. """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

def fix_keyboard_layout(text):
    """ Исправление раскладки (если текст введён латиницей, но должен быть на русском). """
    return text.translate(keyboard_map) if any(c in "qwertyuiopasdfghjklzxcvbnm" for c in text.lower()) else text

ALLOWED_ENGLISH_TERMS = {"Flow", "SberBPM", "Monitor", "GigaChat"}

def is_wrong_layout(text):
    """ Проверка, есть ли смешанная раскладка (кириллица + латиница). """
    words = text.split()
    return any(bool(re.search(r'[а-яА-Я]', word) and re.search(r'[a-zA-Z]', word)) for word in words if word not in ALLOWED_ENGLISH_TERMS)


def fix_typo(text):
    """ Исправление распространённых опечаток. """
    return TYPO_CORRECTIONS.get(text, text)

def smart_text_processing(text):
    """ Полная обработка текста: нормализация, исправление раскладки и устранение опечаток. """
    text = normalize_text(text)
    text = fix_keyboard_layout(text)
    text = fix_typo(text)
    return text
