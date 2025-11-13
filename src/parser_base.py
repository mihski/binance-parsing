from h11 import Data
from pandas import DataFrame
from chrome import get_chrome_driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from io import StringIO
import pandas as pd


class Base_Parser:
    """
    базовый клас для парсинга страниц с таблицаим
    """
    def __init__(self,url: str):

        self.url=url
        self.driver = get_chrome_driver()

    def open_page(self):
        """
        открытие страницы
        """
        self.driver.get(self.url)
        time.sleep(3)
        if self.driver.get(self.url)==None:
            print(f"страница не загрузилась")

        print(f"Открытие страницы: {self.url}")


    def fetch_table(self,xpath:str)-> DataFrame | None:
        """
        извлекаем таблицу
        """
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
        element= self.driver.find_element(By.XPATH,xpath)
        html_content = element.get_attribute('outerHTML')

        tables = pd.read_html(StringIO(html_content))#списик таблиц если их несколько
        table = tables[0]
        print(f"Таблица успешно извлечена ({len(table.columns)} столбцов).")
        return table


    def close(self):
        """Закрывает браузер."""
        if self.driver:
            self.driver.quit()


    def save_table_file():
        pass


