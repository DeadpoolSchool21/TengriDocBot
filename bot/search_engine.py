# search_engine.py

import os
import requests
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

# Инициализация модели для семантического поиска
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

def load_links(path="data/docs_links.txt"):
    """ Загружаем список ссылок на документацию. """
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def extract_text_from_pdf(filepath):
    """ Извлекаем текст из PDF документа. """
    text = ""
    with fitz.open(filepath) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def fetch_text_from_url(url):
    """ Загружаем текст с веб-сайтов и PDF-файлов. """
    if url.startswith("file://"):
        path = url.replace("file://", "")
        return extract_text_from_pdf(path)
    elif url.startswith("http"):
        response = requests.get(url, timeout=10)
        content_type = response.headers.get("Content-Type", "")
        if "pdf" in content_type:
            with open("temp.pdf", "wb") as f:
                f.write(response.content)
            return extract_text_from_pdf("temp.pdf")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text(separator="\n", strip=True)
    return ""

def index_documents(links):
    """ Индексируем загруженные документы для быстрого поиска. """
    indexed = []
    for link in links:
        try:
            text = fetch_text_from_url(link)
            if text:
                embedding = model.encode(text, convert_to_tensor=True)
                indexed.append((link, text, embedding))
            else:
                print(f"⚠️ Документ пустой: {link}")
        except Exception as e:
            print(f"❌ Ошибка обработки {link}: {e}")
    return indexed

def search_query(query, indexed_docs, threshold=0.6):
    """ Улучшенный поиск: повышенный порог точности + ранжирование. """
    query_embedding = model.encode(query, convert_to_tensor=True)
    results = []

    for link, text, embedding in indexed_docs:
        sim = util.cos_sim(query_embedding, embedding).item()
        if sim >= threshold:
            results.append((sim, link, text[:500]))  # Берём релевантную часть текста

    # Сортируем результаты по убыванию точности
    results.sort(reverse=True, key=lambda x: x[0])

    # Берём **ТОЛЬКО 1-2 самых релевантных** фрагмента
    return results[:2] if results else []

