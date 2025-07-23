# bot/strategy.py
from .client import client, symbol
from datetime import datetime, timedelta

def get_opening_range(range_minutes=15):
    now = datetime.utcnow()
    end_time = now.replace(hour=0, minute=range_minutes, second=0, microsecond=0)
    start_time = end_time - timedelta(minutes=range_minutes)

    klines = client.get_kline(
        category="linear",
        symbol=symbol,
        interval="1",
        start=int(start_time.timestamp() * 1000),
        end=int(end_time.timestamp() * 1000),
        limit=range_minutes
    )["result"]["list"]

    highs = [float(k[3]) for k in klines]
    lows = [float(k[4]) for k in klines]
    return max(highs), min(lows)

def execute_orb_trade():
    high, low = get_opening_range()
    last_price = float(client.get_ticker(symbol=symbol)["result"]["lastPrice"])
    
    if last_price > high:
        # Long breakout
        client.place_order(
            category="linear",
            symbol=symbol,
            side="Buy",
            order_type="Market",
            qty=10,
            time_in_force="GoodTillCancel"
        )
        print("LONG triggered")
    elif last_price < low:
        # Short breakout
        client.place_order(
            category="linear",
            symbol=symbol,
            side="Sell",
            order_type="Market",
            qty=10,
            time_in_force="GoodTillCancel"
        )
        print("SHORT triggered")
sss