import os
from chrome import get_chrome_driver
from pages.binance.feerate.locators import FeeRateLocators
from parser_base import Base_Parser

LiquidityProgram =FeeRateLocators.LiquidityProgram


#    Список задач для каждой таблицы
TASKS = [
    {   
        "name": "Spot Maker Program",
        "url": LiquidityProgram.SPOT_MAKER_URL,
        "xpath": LiquidityProgram.SPOT_MAKER_TABLE_XPATH,
        "subfolder": "LiquidityProgram"

    },
    {
        "name": "USDⓈ-M Futures Maker",
        "url": LiquidityProgram.USD_M_FUTUREES_MAKER_URL,
        "xpath": LiquidityProgram.USD_M_FUTUREES_MAKER_XPAT,
        "subfolder": "LiquidityProgram"  
    }
]
parser = Base_Parser()
for task in TASKS:
    parser.open_page(task["url"])
    table=parser.fetch_table(task["xpath"])
    if table is not None:
        print(table.head(2))          # выводим первые 2 строки     

        clean_file_name = task['name'].replace(" ", "_").replace("Ⓢ", "S").replace("-", "_")
        subfolder = task['subfolder'].replace(" ", "_")
        file_path = os.path.join("data", subfolder, f"{clean_file_name}.csv") # <-- file_path   

        should_save , starus_massage = parser.compare_file(table,file_path)
        if should_save== True:           
            parser.save_to_file(table, task['name'],task['subfolder'], directory="data")
            print("***************************")
    else:
        print(f"Таблица {task["name"]}не найдена.")

parser.close()