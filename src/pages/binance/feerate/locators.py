from selenium.webdriver.common.by import By


"""Locators and Urls for Fee Rate"""

class FeeRateLocators:

    SPOT_MAKER_TABLE_XPATH = "//table[contains(., 'Weekly Maker Volume" \
                            " Percentage Requirement')]"

    ALT_LIQUDITY_BOOST_TABLE_XPATH = "//table[contains(., 'User’s Weekly Spot Maker Volume (%) to the Total Binance Spot Maker Volume in Eligible Altcoin Pairs')]"

    ALT_LIQUDITY_BOOST_LOCATOR = (By,ALT_LIQUDITY_BOOST_TABLE_XPATH)

    SPOT_MAKER_LOCATOR= (By,SPOT_MAKER_TABLE_XPATH) 
class FeeRateURLs:
    BASE = "https://www.binance.com"
    SPOT_MAKER_URL = f"{BASE}/en/fee/spotMaker"
    ALT_LIQUDITY_BOOST_URL= f"{BASE}/en/fee/altCoinLiquidityBoost"


