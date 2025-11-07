"""
начинаю парсить
"""

import time
from chrome_driver import setup_driver
from selenium.webdriver.support.ui import WebDriverWait # класс для  явных ожиданий
from selenium.webdriver.support import expected_conditions as EC # класс стандартных
from selenium.webdriver.common.by import By # класс By для поиска элементов по разным стратегиям (CSS, ID, XPATH)
import pandas as pd  # библиотека Pandas для работы с табличными данными
from bs4 import BeautifulSoup

url=f"https://www.binance.com/en/fee/spotMaker"
PREV_DATA_FILE = 'previous_data.json'  # Имя файла для данных предыдущего запроса
TABLE_SELECTOR = (By.TAG_NAME, 'table')  # Стратегия поиска: ищем элемент по тегу <table>
                                         # (By.ID, By.CLASS_NAME)

# def main():
#     """
#     открытие страницы
#     """
#     driver = setup_driver(headless=True)
#     driver.get(url)
#     time.sleep(10)
#     print("Открыта страница:", driver.title)
#     driver.quit()


def fetch_current_data(driver, url):
    """Использует Selenium для загрузки, ожидания, и BeautifulSoup для парсинга."""
    try:
        driver.get(url)  # Загружаем указанный URL
        print("Ожидание загрузки динамического контента...")

        #  ожидание (Selenium):  пока элемент таблицы станет доступен
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TABLE_SELECTOR)
        )

        # 2. Получение HTML (Selenium): Получаем весь HTML-код страницы после ее полной загрузки
        html_content = driver.page_source

        #  Создаем объект BeautifulSoup для разбора HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Находим нужную таблицу с помощью BeautifulSoup (используя тот же селектор)
        table = soup.find(TABLE_SELECTOR[1]) # В TABLE_SELECTOR[1] находится 'table'

        if not table:
            print("Таблица не найдена на странице.")
            return pd.DataFrame() # Возвращаем пустой DataFrame

        # 4. Чтение данных (Pandas): Используем Pandas для прямого чтения HTML-таблицы
        # Передаем Pandas только HTML-код *конкретной* таблицы, а не всей страницы
        dfs = pd.read_html(str(table))
        current_df = dfs[0]  # pd.read_html всегда возвращает список, берем первый элемент

        # Обязательно переименуйте столбцы в соответствии с вашей таблицей
        # ИНАЧЕ Pandas не сможет корректно сравнить их в check_for_changes
        # current_df.columns = ['tier'
        #                       'Weekly Maker Volume Percentage Requirement',
        #                       'And/Or',
        #                       'Weekly Maker Volume (USD equivalent)',
        #                       'Maker Fee (Rebate)',
        #                       'Taker Fees']

        print("Обнаруженные столбцы (по умолчанию):", current_df.columns.tolist())
        return current_df  # Возвращаем DataFrame с текущими данными

    except Exception as e:
        print(f"❌ Ошибка при получении/парсинге данных: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки


def save_data(df, file_path):
    """Сохраняет текущий DataFrame для следующего цикла."""
    df.to_json(file_path, orient='records', indent=4)  # Сохраняем DataFrame в JSON-файл


# --- ВРЕМЕННЫЙ БЛОК ДЛЯ ПРОВЕРКИ ---
if __name__ == "__main__":

    # 1. Запуск драйвера
    driver = setup_driver()

    # 2. Получение данных
    print("Получение данных для первой проверки...")
    data_to_check = fetch_current_data(driver, url)

    # 3. Закрытие драйвера
    driver.quit()

    # 4. Проверка и сохранение
    if not data_to_check.empty:
        # Убедитесь, что у вас есть столбец 'Asset' перед сохранением!
        if 'tier' in data_to_check.columns:
            # Сохраняем файл для просмотра
            save_data(data_to_check, "initial_scrape_data.json")
            print("✅ Данные успешно спарсены и сохранены в initial_scrape_data.json")
            print("\nПервые 5 строк данных:")
            print(data_to_check.head())
        else:
            print("❌ Ошибка: Не удалось найти или назвать столбец 'tier'. Проверьте код парсинга.")
    else:
        print("❌ Не удалось получить данные. Проверьте URL и селектор TABLE_SELECTOR.")