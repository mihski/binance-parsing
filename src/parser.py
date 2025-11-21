import os
from src.parser_base import Base_Parser
from src.binance.feerate.list_pages import list_tables
from src.bybit.locators import BybitLocators

def main_parser():
    parser = Base_Parser()
    for section_list in list_tables.values():
        for tab in section_list:
            parser.open_page(tab["url"])
            table=parser.fetch_table(tab["xpath"])
            if table is not None:
                print(table.head(2))    # выводим первкю строку
                file_path = os.path.join("data", tab['subfolder'], f"{tab['name']}.csv")
                should_save , status_massage = parser.compare_file(table,file_path)
                if should_save == True:
                    print( status_massage)
                    parser.save_to_file(table, tab['name'],tab['subfolder'], directory="data")
                    print("***************************")
            else:
                print(f"Таблица {tab["name"]} не найдена.")
    parser.close()


def check_data_from_bybit():

    url = BybitLocators.DATA_URL
    xpath= BybitLocators.DETA_XPART

    parser = Base_Parser()
    parser.open_page(url)
    parser.fetch_text(xpath)

if __name__ == "__main__" :
   check_data_from_bybit()