

# Import flask module
from flask import Flask, render_template

from data_sources.binance_ import Binance

app = Flask(__name__)


@app.route('/')
def run():
    binance_connect = Binance()
    return render_template('index.html',
                           time=binance_connect.get_time(),
                           minute_kline=binance_connect.get_minute_kline(),
                           hourly_kline=binance_connect.get_hourly_kline()
                           # new_client_account=binance_connect.get_new_client_account(),
                           # with_params=binance_connect.get_with_params()
                           )


# main driver function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)