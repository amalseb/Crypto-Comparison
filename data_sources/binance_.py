from binance.spot import Spot


class Binance:
    def __init__(self):
        self.client = Spot()

    def get_historical_trades(self):
        return self.client.historical_trades("BTCUSDT")

