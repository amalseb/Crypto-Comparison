# Import flask module
from flask import Flask, render_template

from binance_ import Binance
from coinbase_ import Coinbase

app = Flask(__name__)


@app.route('/')
def run():
    binance_connect = Binance()
    coinbase_connect = Coinbase()
    return render_template('index.html',
                           bin=binance_connect.get_historical_trades(),
                           cb=coinbase_connect.get_historical_trades())


# main driver function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
