from selenium.webdriver.common.by import By



"""Locators and Urls"""

class LocatorLiquidityProgram:
    LIQUIDITY_TABLE_XPATH = "//table[contains(., 'Weekly Maker Volume" \
                            " Percentage Requirement')]"
    LOCATOR_LIQUIDITY = (By,LIQUIDITY_TABLE_XPATH)


