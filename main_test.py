"""
начинаю парсить
"""

import time
from io import StringIO
from chrome_driver import setup_driver
from selenium.webdriver.support.ui import WebDriverWait # класс для  явных ожиданий
from selenium.webdriver.support import expected_conditions as EC # класс стандартных
from selenium.webdriver.common.by import By # класс By для поиска элементов по разным стратегиям (CSS, ID, XPATH)
import pandas as pd  # библиотека Pandas для работы с табличными данными
from bs4 import BeautifulSoup

url=f"https://www.binance.com/en/fee/spotMaker"
PREV_DATA_FILE = 'previous_data.json'  # Имя файла для данных предыдущего запроса
TARGET_TABLE_XPATH = "//table[contains(., 'Weekly Maker Volume Percentage Requirement')]"
TARGET_LOCATOR = (By.XPATH, TARGET_TABLE_XPATH)
TAIMEOUT=10
driver=setup_driver
def fetch_current_data(driver, url):

    try:
        driver.get(url)
        print("Ожидание загрузки динамического контента...")

        #  ожидание (Selenium):  пока элемент таблицы станет доступен
        WebDriverWait(driver, TAIMEOUT).until(
            EC.presence_of_element_located(TARGET_LOCATOR)
        )

        table_element = driver.find_element(*TARGET_LOCATOR)

        html_content = table_element.get_attribute('outerHTML')
        # Чтение данных (Pandas с StringIO)
        dfs = pd.read_html(StringIO(html_content))
        current_df = dfs[0]
        print(f"количество столбцов найдено{len(current_df.columns)}")

        # 3. Обработка столбцов

        new_columns = [
            'Tier',
            'Weekly_Per_Req',
            'And/or',
            'Weekly_USD equivalent',
            'Maker_Fees',
            'Taker_Fees'
        ]
        if len(current_df.columns) == len(new_columns):
            current_df.columns = new_columns

            print("✅ DataFrame успешно создан (6 столбцов найдено и переименовано).")
        else:
        # Этот блок сработает, если Pandas найдет 5, 7 или 8 столбцов
            print(f"⚠️ ВНИМАНИЕ: Ожидалось 6 столбцов, но Pandas нашел {len(current_df.columns)}. Проверьте структуру.")

    except Exception as e:
         print(f"❌ Ошибка при получении/парсинге данных: {e}")


if __name__ == "__main__":

    driver = setup_driver()
    fetch_current_data(driver, url)
