import os
from src.parser_base import Base_Parser
from src.bybit.locators import BybitLocators

def text_parser():

    url = BybitLocators.DATA_URL
    xpath= BybitLocators.DETA_XPART

    parser = Base_Parser()
    parser.open_page(url)
    parser.fetch_text(xpath)



