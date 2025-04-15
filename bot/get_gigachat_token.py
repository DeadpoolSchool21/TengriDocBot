# get_gigachat_token.py

import requests
import uuid
import time
import threading
import urllib3

# Отключаем предупреждения SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Данные клиента
AUTH_KEY = "NjJjMzY5NTAtMmI1YS00ZDIyLTk3NDUtYWVhM2FiMTFlMGU4OjM5ZTZlYmIyLTAwYTEtNGE0MC04NDg2LTliOTVkYTBlZGM0OA=="  
TOKEN_UPDATE_INTERVAL = 1800  # 30 минут

class GigaChatAuth:
    """ Автоматическое обновление токена GigaChat каждые 30 минут. """

    def __init__(self):
        self.access_token = self.get_gigachat_token()
        self.start_auto_refresh()

    def get_gigachat_token(self):
        """ Запрашивает новый Access Token. """
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
            "Authorization": f"Basic {AUTH_KEY}"
        }
        payload = {"scope": "GIGACHAT_API_PERS"}

        response = requests.post(url, headers=headers, data=payload, verify="/Users/peterallen/TengriDocBot/gigachat.crt")

        if response.status_code == 200:
            token = response.json().get("access_token")
            print(f"✅ Получен новый токен GigaChat: {token}")  # Показываем токен в консоли
            return token
        else:
            print(f"❌ Ошибка получения токена: {response.status_code} - {response.text}")
            return None

    def start_auto_refresh(self):
        """ Запускает процесс автообновления токена. """
        def updater():
            while True:
                time.sleep(TOKEN_UPDATE_INTERVAL)
                self.access_token = self.get_gigachat_token()
                print(f"🔄 Обновлён токен GigaChat: {self.access_token}")  # Выводим обновлённый токен

        threading.Thread(target=updater, daemon=True).start()

# Экземпляр для управления токеном
gigachat_auth = GigaChatAuth()

# Проверяем, сохранился ли токен
print(f"🛠 Debug [get_gigachat_token.py]: gigachat_auth.access_token = {gigachat_auth.access_token}")
