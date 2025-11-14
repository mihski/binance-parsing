from pyclbr import Class
from selenium.webdriver.common.by import By
#   https://www.binance.com/en/fee

"""Locators and Urls for Fee Rate"""

class FeeRateLocators:
    """локаторов для раздела Fee Rate """
    BASE = "https://www.binance.com"

    class LiquidityProgram:
        BASE = "https://www.binance.com"
        ALT_LIQUDITY_BOOST_URL= f"{BASE}/en/fee/altCoinLiquidityBoost"
        SPOT_MAKER_URL = f"{BASE}/en/fee/spotMaker"
        USD_M_FUTUREES_MAKER_URL= f"{BASE}/en/fee/umMaker"


        ALT_LIQUDITY_BOOST_TABLE_XPATH = "//div[@id='bn-tab-pane-1']//table"
        SPOT_MAKER_TABLE_XPATH ="//div[@id='bn-tab-pane-0']//table"
        USD_M_FUTUREES_MAKER_XPAT = "//div[@id='bn-tab-pane-2']//table"



        ALT_LIQUDITY_BOOST_LOCATOR= (By,ALT_LIQUDITY_BOOST_TABLE_XPATH)
        USD_M_FUTUREES_LOCATOR = (By,ALT_LIQUDITY_BOOST_TABLE_XPATH)
        SPOT_MAKER_LOCATOR= (By,SPOT_MAKER_TABLE_XPATH)

    class Trading:
        pass



