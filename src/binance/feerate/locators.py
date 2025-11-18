from pyclbr import Class
from selenium.webdriver.common.by import By
#   https://www.binance.com/en/fee

"""Locators and Urls for Fee Rate"""

class FeeRateLocators:
    """локаторов для раздела Fee Rate """
    BASE = "https://www.binance.com"

    class LiquidityProgram:
        BASE = "https://www.binance.com/en/fee"

        SPOT_MAKER_URL = f"{BASE}/spotMaker"
        SPOT_MAKER_TABLE_XPATH ="//div[@id='bn-tab-pane-0']//table"

        ALT_LIQUDITY_BOOST_URL= f"{BASE}/altCoinLiquidityBoost"
        ALT_LIQUDITY_BOOST_TABLE_XPATH = "//div[@id='bn-tab-pane-1']//table"

        USD_M_FUTUREES_MAKER_URL= f"{BASE}/umMaker"
        USD_M_FUTUREES_MAKER_XPAT = "//div[@id='bn-tab-pane-2']//table"

        COIN_M_FUTUREES_MAKER_URL= f"{BASE}/cmMaker"
        COIN_M_FUTUREES_MAKER_XPAT = "//div[@id='bn-tab-pane-3']//table"


    class Trading:
        BASE = "https://www.binance.com/en/fee"

        SPOT_MARJIN_URL = f"{BASE}/trading"
        SPOT_MARJIN_XPATH ="//div[@id='bn-tab-pane-0']//table"



        pass



