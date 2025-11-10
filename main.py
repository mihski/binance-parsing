"""
создание начального файла
"""
import os
from io import StringIO
from selenium.webdriver.support.ui import WebDriverWait # класс для  явных ожиданий
from chrome_driver import setup_driver
import pandas as pd  # библиотека Pandas для работы с табличными дан
from selenium.webdriver.support import expected_conditions as EC # класс стандартных
from selenium.webdriver.common.by import By # класс By для поиска элементов по разным стратегиям (CSS, ID, XPATH)
from telrga_bot import send_telegram_message

url=f"https://www.binance.com/en/fee/spotMaker"
SAVE_DATA_FILE = 'save_data.json'  # Имя файла для данных предыдущего запроса
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
        print(f"количество найденых столбцов: {len(current_df.columns)}")

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
            print(f"⚠️ ВНИМАНИЕ: Ожидалось 6 столбцов, но Pandas нашел {len(current_df.columns)}.")

    except Exception as e:
         print(f"❌ Ошибка при получении/парсинге данных: {e}")
    return current_df

def save_data():
    if not current_data_df.empty:
        print("\n--- Результат парсинга ---")
        print(current_data_df)
        print("--------------------------")
        current_data_df.to_json(
            SAVE_DATA_FILE,
            orient='records',
            indent=4
        )

def compare_data(current_df, prev_data_file):
    """
    Загружает предыдущие данные из JSON и сравнивает их с текущим DataFrame.
    """
    if not os.path.exists(prev_data_file):
        print("📁 Первый запуск. Файл предыдущих данных не найден.")
        return True, "INITIAL_RUN" # Возвращаем True, чтобы сохранить текущие данные

    try:
        # Загрузка предыдущих данных из JSON (используем те же параметры, что и для сохранения)
        prev_df = pd.read_json(prev_data_file, orient='records')

        # Убедимся, что оба DataFrame имеют одинаковый порядок строк/столбцов перед сравнением
        prev_df = prev_df.sort_index(axis=1)
        current_df = current_df.sort_index(axis=1)

        # Сравнение: Pandas .equals() сравнивает каждый элемент
        if current_df.equals(prev_df):
            print("✅ Данные не изменились.  'Liquidity Program' стабильна.")

            return False, "NO_CHANGE"
        else:
            send_telegram_message("ВНИМАНИЕ: Обнаружены изменения в таблице! ")
            print("🚨 ВНИМАНИЕ: Обнаружены изменения в таблице!")

            # Дополнительный вывод для отладки: показываем, что изменилось
            # .merge() позволяет найти различия между двумя DF
            comparison_df = current_df.merge(
                prev_df,
                indicator=True,
                how='outer'
            ).query('_merge != "both"')

            print("\n--- Отличия (новые или удаленные строки) ---")
            print(comparison_df)
            print("---------------------------------------------")
            return True, "CHANGED"

    except Exception as e:
        print(f"❌ Ошибка при сравнении данных или чтении файла: {type(e).__name__} - {e}")
        return True, "ERROR_OCCURRED" # В случае ошибки (например, поврежден JSON), сохраняем новые данные

if __name__ == "__main__":
    # Убедитесь, что PREV_DATA_FILE определен в глобальной области
    # PREV_DATA_FILE = 'previous_data.json'

    driver = None
    try:
        driver = setup_driver()
        current_data_df = fetch_current_data(driver, url)

        if current_data_df is None or current_data_df.empty:
            print("Пропуск сравнения: не удалось получить текущие данные.")

        else:
            # 1. Сравнение с предыдущими данными
            should_save, status = compare_data(current_data_df, SAVE_DATA_FILE)

            # 2. Условное сохранение
            if should_save:
                current_data_df.to_json(
                    SAVE_DATA_FILE,
                    orient='records',
                    indent=4
                )
                print(f"\n💾 Новые данные сохранены в {SAVE_DATA_FILE} (Статус: {status}).")
            else:
                send_telegram_message("Таблица 'Liquidity Program' не изменились ")

    finally:
        if driver:
            driver.quit()
