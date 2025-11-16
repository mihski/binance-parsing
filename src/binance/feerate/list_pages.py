from binance.feerate.locators import FeeRateLocators
LiquidityProgram =FeeRateLocators.LiquidityProgram

#    Список задач для каждой таблицы
list_tables = [
    {   
        "name": "SpotMakerProgram",
        "url": LiquidityProgram.SPOT_MAKER_URL,
        "xpath": LiquidityProgram.SPOT_MAKER_TABLE_XPATH,
        "subfolder": "LiquidityProgram"
    },
    {
        "name": "USDWS_M_FuturesMaker",
        "url": LiquidityProgram.USD_M_FUTUREES_MAKER_URL,
        "xpath": LiquidityProgram.USD_M_FUTUREES_MAKER_XPAT,
        "subfolder": "LiquidityProgram"  
    }
]