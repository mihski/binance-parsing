from chrome import get_chrome_driver
from pages.binance.feerate.locators import FeeRateLocators
from parser_base import Base_Parser

LiquidityProgram =FeeRateLocators.LiquidityProgram


#    Список задач для каждой таблицы
TASKS = [
    {
        "name": "USDⓈ-M Futures Maker",
        "url": LiquidityProgram.USD_M_FUTUREES_MAKER_URL,
        "xpath": LiquidityProgram.USD_M_FUTUREES_MAKER_XPAT
    },
    {
        "name": "Spot Maker Program",
        "url": LiquidityProgram.SPOT_MAKER_URL,
        "xpath": LiquidityProgram.SPOT_MAKER_TABLE_XPATH
    }
]
parser = Base_Parser()
for task in TASKS:
    parser.open_page(task["url"])
    table=parser.fetch_table(task["xpath"])
    if table is not None:
        print(table.head(2))          # выводим первые 2 строки
        print("***************************")
    else:
        print(f"Таблица {task["name"]}не найдена.")


parser.close()