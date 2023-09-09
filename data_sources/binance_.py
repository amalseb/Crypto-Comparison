from binance.spot import Spot


class Binance:
    def __init__(self):
        self.client = Spot()

    def get_time(self):
        return self.client.time()

    def get_minute_kline(self):
        return self.client.klines("BTCUSDT", "1m")

    def get_hourly_kline(self):
        return self.client.klines("BNBUSDT", "1h", limit=10)

    # def get_new_client_account(self):
    #     return self.new_client.account()
    #
    # def get_with_params(self):
    #     params = {
    #         "symbol": "BTCUSDT",
    #         "side": "SELL",
    #         "type": "LIMIT",
    #         "timeInForce": "GTC",
    #         "quantity": 0.002,
    #         "price": 9500
    #     }
    #
    #     response = self.new_client.new_order(**params)
    #     return response
