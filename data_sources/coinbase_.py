from coinbase.wallet.client import Client


class Coinbase:
    def __init__(self):
        self.client = Client("", "")

    def get_historical_trades(self):
        price = self.client.get_historic_prices(currency_pair='BTC-USD')
        return price