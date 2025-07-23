# bot/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from .strategy import execute_orb_trade

scheduler = BackgroundScheduler()

def start():
    scheduler.add_job(execute_orb_trade, "cron", hour=0, minute=15)  # Run once after open
    scheduler.start()

def stop():
    scheduler.shutdown()
