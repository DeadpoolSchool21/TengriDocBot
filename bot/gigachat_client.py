# gigachat_client.py

import requests
from bot.get_gigachat_token import gigachat_auth  # Используем автообновляемый токен

class GigaChatClient:
    """ Класс для взаимодействия с GigaChat API. """

    BASE_URL = "https://gigachat.devices.sberbank.ru/api/v1"

    def __init__(self):
        print("🛠 Debug [gigachat_client.py]: Принудительно загружаем токен GigaChat...")
        gigachat_auth.access_token = gigachat_auth.get_gigachat_token()  # Запрашиваем новый токен
        self.access_token = gigachat_auth.access_token
        print(f"🔹 [gigachat_client.py] Используем токен GigaChat: {self.access_token}")

    def ask_gigachat(self, prompt):
        """ Отправляет запрос в GigaChat и получает ответ. """
        url = f"{self.BASE_URL}/chat/completions"

        # Отладка: проверяем, передаётся ли токен
        print(f"🛠 Debug [gigachat_client.py]: gigachat_auth.access_token = {gigachat_auth.access_token}")

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {gigachat_auth.access_token}"  # Используем актуальный токен!
        }
        payload = {
            "model": "gigachat_latest",
            "messages": [
                {"role": "system", "content": "Ты — AI-помощник, отвечающий строго по документации."},
                {"role": "user", "content": prompt}
            ]
        }

        print(f"🔹 Используем токен GigaChat: {gigachat_auth.access_token}")

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Не удалось получить ответ.")
        else:
            print(f"❌ Ошибка GigaChat: {response.status_code} - {response.text}")
            return "⚠️ Ошибка при обращении к GigaChat."

# Создаём единственный экземпляр клиента
gigachat_client = GigaChatClient()
