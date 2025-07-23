# nexbit



✅ Here's the high-level structure:

🧠 ORB Strategy (Opening Range Breakout)

Define an opening time window (e.g., first 15 minutes after market opens).

Capture high and low during this range.

Go long if price breaks above the high, short if below the low.

Set TP/SL based on volatility or ATR (Average True Range).

Optionally use 1-minute candles for precision.

🧱 Architecture Outline
🔁 Backend (Python)
Use FastAPI or Flask

Connect to Bybit Testnet API via ccxt or pybit

Run strategy as a scheduled job or live WebSocket handler

REST endpoints:

```bash
/start-bot

/stop-bot

/get-status

/get-trades
```

Store logs in SQLite or JSON

Manage keys via .env

🌐 Frontend (React)
Dashboard:

Start/Stop bot

Show current position

Show opening range

Table of historical trades

WebSocket or polling for live updates

Chart.js or Recharts to display SUI price

```bash

orb-bot/
├── bot/
│   ├── strategy.py
│   ├── client.py
│   └── scheduler.py
├── main.py
├── .env
├── requirements.txt

```
