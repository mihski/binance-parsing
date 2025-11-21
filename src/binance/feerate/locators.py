# from pyclbr import Class
# from selenium.webdriver.common.by import By
#   https://www.binance.com/en/fee

"""Locators and Urls for Fee Rate"""

class FeeRateLocators:
    """локаторов для раздела Fee Rate """
    BASE = "https://www.binance.com"
    NAME_MARCET= "binance"

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

        FUTURES_USD_M_URL = f"{BASE}/futureFee"
        FUTURES_USD_M_XPATH = "//div[@id='bn-tab-pane-1']//table"

        FUTURES_COIN_M_URL = f"{BASE}/deliveryFee"
        FUTURES_COIN_M_XPATH = "//div[@id='bn-tab-pane-2']//table"

        OPTIONS_URL = f"{BASE}/optionsTrading"
        OPTIONS_XPATH = "//div[@id='bn-tab-pane-3']//table"

        NFT_URL = f"{BASE}/nftFee"
        NFT_XPATH = "//div[@id='bn-tab-pane-4']//table"

        P2P_URL = f"{BASE}/p2pFeeRate"
        P2P_XPATH = "//div[@id='bn-tab-pane-5']//table"

        FIAT_URL = f"{BASE}/fiatSpot"
        FIAT_XPATH = "//div[@id='bn-tab-pane-6']//table"

    class SpotPromotions:
        BASE = "https://www.binance.com/en/fee"

        ZERO_FEE_URL = f"{BASE}/tradingPromote"
        ZERO_FEE_TABLE_XPATH ="//div[@id='bn-tab-pane-0']//table"

        FDUSD_URL = f"{BASE}/fdusd"
        FDUSD_TABLE_XPATH ="//div[@id='bn-tab-pane-1']//table"

        EUROPROMO_URL = f"{BASE}/eur"
        EUROPROMO_TABLE_XPATH ="//div[@id='bn-tab-pane-2']//table"

        USDCPROMO_URL = f"{BASE}/usdcPromo"
        USDCPROMO_TABLE_XPATH ="//div[@id='bn-tab-pane-3']//table"










