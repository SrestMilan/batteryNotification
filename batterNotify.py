""""
import psutil  # retrieve battery notification
from plyer import notification # shows battery notification
import time

lowBattery=15     # low battery level
fullBattery=100   # full battery level
checkInterval=60  # check battery every 60 seconds
"""
from plyer import notification

notification.notify(
    title="Test",
    message="Plyer is working",
    app_name="MyApp",
    timeout=10
)

