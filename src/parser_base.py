import os
from h11 import Data
from pandas import DataFrame
from src.chrome import get_chrome_driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from io import StringIO
import pandas as pd
from src.tg_alerting.telrgam_bot import send_telegram_message
from src.tg_alerting.config import CHAT_ID_ERRORS,CHAT_ID_UPDATES



class Base_Parser:
    """
    базовый клас для парсинга страниц с таблицаим
    """
    def __init__(self):
        self.driver = get_chrome_driver()
        self.url = None

    def open_page(self,url:str):
        """
        открытие страницы
        """
        self.url = url
        self.driver.get(self.url)
        print(f"Открытие страницы: {self.url}")
        time.sleep(2)


    def _get_element(self, xpath: str, timeout: int = 10):
        """
        Приватный ,базовый метод для всех элементов: ждет и возвращает WebElement.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return self.driver.find_element(By.XPATH, xpath)
        except TimeoutException:
            print(f"❌ Элемент не найден по XPath: {xpath} (Timeout)")
            return None


    def fetch_text(self, xpath: str, timeout: int = 10) -> str | None:
        """
        извлечение текста из любого элемента
        (даты, заголовки, цены и т.д.)
        """
        print(f"⏳ Ожидаем текст по XPath: {xpath}")
        element = self._get_element(xpath, timeout)

        if element:
            text = element.text.strip() # убирает лишние пробелы
            print(f"Текст успешно извлечен: '{text}'")
            return text
        return None

    def fetch_table(self,xpath:str,timeout=10)-> DataFrame | None:
        """
        извлекаем таблицу
        """
        print(f"⏳ Ожидаем таблицу по XPath: {xpath}")
        element= self._get_element(xpath, timeout)

        if element !=None:
            try:

                html_content = element.get_attribute('outerHTML')
                tables = pd.read_html(StringIO(html_content))#списик таблиц если их несколько
                table = tables[0]
                print(f"Таблица успешно извлечена ({len(table.columns)} столбцов).")
                return table

            except TimeoutException:
            #    send_telegram_message(f"Не удалось дождаться загрузки таблицы ",CHAT_ID_ERRORS)
                print("❌ Не удалось дождаться загрузки таблицы (Timeout).")
                return None
        return None

    def close(self):
        """Закрывает браузер."""
        if self.driver:
            self.driver.quit()

    def save_to_file(self, table_data: DataFrame,
                     file_name: str, subfolder:str,
                     directory: str = "data", ):
        """
        Сохраняет DataFrame в CSV файл. Создает каталог, если он не существует.

        """

        full_directory_path = os.path.join(directory,subfolder)
        file_path = os.path.join(full_directory_path, f"{file_name}.csv")

        try:
            os.makedirs(full_directory_path,exist_ok=True)
            table_data.to_csv(file_path, index=False, encoding='utf-8')
            print(f"💾 Данные успешно сохранены в: {file_path}")
            return file_path
        except Exception as e:
            print(f"❌ Ошибка при сохранении файла {file_name}: {e}")

        def close(self):
            # ... (остальной код close)
            pass

    def compare_file(self,current_df,saved_data_file):
        if not os.path.exists(saved_data_file):
            print("📁 Первый запуск. Файл предыдущих данных не найден.")
            return True, "INITIAL_RUN" # Возвращаем True, чтобы сохранить текущие данные

        try:
            saved_df = pd.read_csv(saved_data_file, encoding='utf-8')

        except Exception as e:
            print(f"⚠️ Ошибка чтения старого файла {saved_data_file}: {e}")
        #    send_telegram_message(f"Ошибка чтения сохраненного файла {saved_data_file}",CHAT_ID_ERRORS)
            return True, "READ_ERROR"

        if current_df.equals(saved_df):
            print("файл не изменен")
            return False, "NO_CHANGE"
        else:
            print("файл  изменен")

         #   send_telegram_message(f"изменилась таблица {saved_data_file}",CHAT_ID_UPDATES)

            return True, "CHANGED"






