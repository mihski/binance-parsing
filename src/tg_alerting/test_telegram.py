from src.tg_alerting.config import CHAT_ID_ERRORS,CHAT_ID_UPDATES
from src.tg_alerting.telrgam_bot import send_telegram_message

if __name__ == "__main__":

    send_telegram_message("Проверка отправки в Updates",CHAT_ID_UPDATES)
    send_telegram_message("Проверка отправки в Erorr",CHAT_ID_ERRORS)

