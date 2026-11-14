import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "Hunterd на связи! 🕵️ Бот успешно подключён."
})

response.raise_for_status()
print("Сообщение отправлено!")
