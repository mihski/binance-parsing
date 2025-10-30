import os
from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://www.binance.com/en/fee/spotMaker"

SAVE_DATA_FILE = "save_data_file.js