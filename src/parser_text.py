import os
from src.parser_base import Base_Parser
from src.bybit.locators import BybitLocators

def text_parser():

    url = BybitLocators.DATA_URL
    xpath= BybitLocators.DETA_XPART

    parser = Base_Parser()
    parser.open_page(url)
    text_date=parser.fetch_text(xpath)
    parser.save_text_to_file(text_date,"date","bybit","data")




