
import psutil  # retrieve battery information
from plyer import notification  # show notifications
import time

lowBattery = 15 # trigger low battery 
fullBattery = 100 # trigger full battery
checkInterval = 60 #checks time interval

def retrieve_battery_status():
    val_battery = psutil.sensors_battery()  # read battery info

    print(f"Battery level is {val_battery.percent}%")
    print(f"Charging: {val_battery.power_plugged}")

    return val_battery.percent, val_battery.power_plugged

def notify_text(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=6
    )

 