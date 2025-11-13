from selenium.webdriver.common.by import By


"""Locators and Urls for Fee Rate"""

class FeeRateLocators:

    SPOT_MAKER_TABLE_XPATH = "//table[contains(., 'Weekly Maker Volume" \
                            " Percentage Requirement')]"
    SPOT_MAKER_LOCATOR= (By,SPOT_MAKER_TABLE_XPATH)


class FeeRateURLs:
    BASE = "https://www.binance.com"
    SPOT_MAKER = f"{BASE}/en/fee/spotMaker"



