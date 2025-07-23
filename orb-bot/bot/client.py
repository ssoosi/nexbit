# bot/client.py
from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv

load_dotenv()

client = HTTP(
    testnet=True,
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET")
)

symbol = os.getenv("SYMBOL", "SUIUSDT")
