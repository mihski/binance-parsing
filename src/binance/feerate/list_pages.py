from src.binance.feerate.locators import FeeRateLocators
LiquidityProgram = FeeRateLocators.LiquidityProgram
Trading = FeeRateLocators.Trading
SpotPromotions= FeeRateLocators.SpotPromotions

#    Список таблиц внутри разделов
list_tables = {
        "LiquidityProgram":[
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
        ],

        "Trading": [
            {
                "name": "Spot_margin",
                "url": Trading.SPOT_MARJIN_URL,
                "xpath": Trading.SPOT_MARJIN_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "Futures_USD_M",
                "url": Trading.FUTURES_USD_M_URL,
                "xpath": Trading.FUTURES_USD_M_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "Futures_COIN_M",
                "url": Trading.FUTURES_COIN_M_URL,
                "xpath": Trading.FUTURES_COIN_M_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "Options",
                "url": Trading.OPTIONS_URL,
                "xpath": Trading.OPTIONS_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "NFT",
                "url": Trading.NFT_URL,
                "xpath": Trading.NFT_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "P2P",
                "url": Trading.P2P_URL,
                "xpath": Trading.P2P_XPATH,
                "subfolder": "Trading"
            },
            {
                "name": "Fiat",
                "url": Trading.FIAT_URL,
                "xpath": Trading.FIAT_XPATH,
                "subfolder": "Trading"
            },
        ],
     "SpotPromotions":[
         {
            "name": "ZeroFee",
            "url": SpotPromotions.ZERO_FEE_URL,
            "xpath": SpotPromotions.ZERO_FEE_TABLE_XPATH,
            "subfolder": "SpotPromotions"
        },
        {
            "name": "FDUSD",
            "url": SpotPromotions.FDUSD_URL,
            "xpath": SpotPromotions.FDUSD_TABLE_XPATH,
            "subfolder": "SpotPromotions"
        },
        {
            "name": "EuroPromo",
            "url": SpotPromotions.EUROPROMO_URL,
            "xpath": SpotPromotions.EUROPROMO_TABLE_XPATH,
            "subfolder": "SpotPromotions"
        },
        {
            "name": "USDCPromo",
            "url": SpotPromotions.USDCPROMO_URL,
            "xpath": SpotPromotions.USDCPROMO_TABLE_XPATH,
            "subfolder": "SpotPromotions"
        }
     ]
}
