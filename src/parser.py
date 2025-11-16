import os
from src.binance.feerate.locators import FeeRateLocators
from src.parser_base import Base_Parser
from src.binance.feerate.list_pages import list_tables

def main_parser():
    parser = Base_Parser()
    for tab in list_tables:
        parser.open_page(tab["url"])
        table=parser.fetch_table(tab["xpath"])
        if table is not None:
            print(table.head(1))    # выводим первкю строку            
            file_path = os.path.join("data", tab['subfolder'], f"{tab['name']}.csv")   
            should_save , status_massage = parser.compare_file(table,file_path)
            if should_save == True: 
                print( status_massage)          
                parser.save_to_file(table, tab['name'],tab['subfolder'], directory="data")
                print("***************************")
        else:
            print(f"Таблица {tab["name"]}не найдена.")
    parser.close()

if __name__ == "__main__" :
    main_parser()