from binance.spot import Spot


class Binance:
    def __init__(self):
        self.client = Spot()

    def get_historical_trades(self):
        prices = self.client.historical_trades("BTCUSDT")
        return {"base": "BTC",
                "currency": "USD",
                "prices": [{"price": entry["price"], "time": str(entry["time"])} for entry in prices]}
