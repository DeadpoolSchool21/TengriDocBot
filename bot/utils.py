# utils.py

import re
import string

def normalize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

def is_wrong_layout(text):
    # Проверка, есть ли латиница и кириллица вместе
    return bool(re.search(r'[а-яА-Я]', text) and re.search(r'[a-zA-Z]', text))