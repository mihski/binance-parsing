from src.binance.feerate.locators import FeeRateLocators
LiquidityProgram = FeeRateLocators.LiquidityProgram

#    Список задач для каждой таблицы
list_tables = [
    
    {
        "name": "SpotMakerProgram",
        "url": LiquidityProgram.SPOT_MAKER_URL,
        "xpath": LiquidityProgram.SPOT_MAKER_TABLE_XPATH,
        "subfolder": "LiquidityProgram"
    },
    {
        "name":"AltLiqidityBoost",
        "url": LiquidityProgram.ALT_LIQUDITY_BOOST_URL,
        "xpath": LiquidityProgram.ALT_LIQUDITY_BOOST_TABLE_XPATH,
        "subfolder": "LiquidityProgram"
    },

    {
        "name": "USD_M_FuturesMaker",
        "url": LiquidityProgram.USD_M_FUTUREES_MAKER_URL,
        "xpath": LiquidityProgram.USD_M_FUTUREES_MAKER_XPAT,
        "subfolder": "LiquidityProgram"
    },
     {
        "name": "COIN_M_FuturesMaker",
        "url": LiquidityProgram.COIN_M_FUTUREES_MAKER_URL,
        "xpath": LiquidityProgram.COIN_M_FUTUREES_MAKER_XPAT,
        "subfolder": "LiquidityProgram"
    }



]