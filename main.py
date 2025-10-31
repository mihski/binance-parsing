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
        current_df.columns = ['tier'
                              'Weekly Maker Volume Percentage Requirement',
                              'And/Or',
                              'Weekly Maker Volume (USD equivalent)',
                              'Maker Fee (Rebate)',
                              'Taker Fees']

        return current_df  # Возвращаем DataFrame с текущими данными

    except Exception as e:
        print(f"❌ Ошибка при получении/парсинге данных: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки
    