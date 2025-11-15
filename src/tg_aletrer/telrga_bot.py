from env import TG_BOT_TOKEN
import requests

# TODO: in .env
CHAT_ID="410455335"
def send_telegram_message(message_text):
    """Отправляет сообщение через Telegram API."""
    
    # URL для отправки сообщения (используем стандартный метод sendMessage)
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"

    
    # Параметры запроса
    params = {
        "chat_id": CHAT_ID,
        "text": message_text,
        "parse_mode": "HTML" # Позволяет использовать HTML-теги для форматирования
    }
    
    try:
        response = requests.post(url, data=params)
        response.raise_for_status() # Вызывает ошибку, если запрос не удался
        # print("✅ Сообщение Telegram отправлено.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Не удалось отправить сообщение Telegram: {e}")

if __name__ == "__main__":
    send_telegram_message("hello")