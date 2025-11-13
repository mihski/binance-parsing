from chrome import get_chrome_driver
from pages.binance.feerate.locators import FeeRateURLs,FeeRateLocators
from parser_base import Base_Parser

url= FeeRateURLs.ALT_LIQUDITY_BOOST_URL
#url= FeeRateURLs.SPOT_MAKER
# locator = FeeRateLocators.SPOT_MAKER_LOCATOR
# TABLE_XPATH =FeeRateLocators.SPOT_MAKER_TABLE_XPATH
locator = FeeRateLocators.ALT_LIQUDITY_BOOST_TABLE_XPATH
TABLE_XPATH =FeeRateLocators.ALT_LIQUDITY_BOOST_TABLE_XPATH

parser = Base_Parser(url)
parser.open_page()
table=parser.fetch_table(TABLE_XPATH)
if table is not None:
    print(table.head())          # выводим первые 5 строк
    print(table.columns.tolist()) # выводим заголовки столбцов
else:
    print("Таблица не найдена.")