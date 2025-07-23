# main.py
from fastapi import FastAPI
from bot import scheduler

app = FastAPI()
bot_running = False

@app.get("/start-bot")
def start_bot():
    global bot_running
    if not bot_running:
        scheduler.start()
        bot_running = True
        return {"message": "Bot started"}
    return {"message": "Bot already running"}

@app.get("/stop-bot")
def stop_bot():
    global bot_running
    if bot_running:
        scheduler.stop()
        bot_running = False
        return {"message": "Bot stopped"}
    return {"message": "Bot not running"}

@app.get("/")
def root():
    return {"message": "ORB Trading Bot Running"}
