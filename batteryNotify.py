import psutil                 # Used to access system and battery information
from plyer import notification # Used to display desktop notifications
import time                   # Used to pause the program between battery checks
# ----------------------------
# Configuration Settings
# ----------------------------
LOW_BATTERY = 20      # Alert when battery falls to 20% or below
FULL_BATTERY = 100    # Alert when battery reaches 100%
CHECK_INTERVAL = 60   # Check battery status every 60 seconds
# ----------------------------
# Function: Get Battery Status
# ----------------------------
def get_battery_status():
    """
    Retrieves current battery information from the system.

    Returns:
        percent (int): Current battery percentage.
        power_plugged (bool): True if charger is connected, False otherwise.
    """
    battery = psutil.sensors_battery()
    # Return battery percentage and charging status
    return battery.percent, battery.power_plugged
# ----------------------------
# Function: Show Notification
# ----------------------------

def show_notification(title, message):
    """
    Displays a desktop notification.

    Parameters:
        title (str): Notification title.
        message (str): Notification message.
    """

    notification.notify(
        title=title,
        message=message,
        timeout=5  # Notification remains visible for 5 seconds
    )
# ----------------------------
# Main Program
# ----------------------------
def main():
    # Stores last notification type
    # Prevents the same notification from appearing repeatedly
    last_alert = None
    # Infinite loop to continuously monitor battery
    while True:
        # Get current battery percentage and charging status
        percent, plugged = get_battery_status()

        # Display current battery status in terminal
        print(f"Battery: {percent}% | Charging: {plugged}")

        # ----------------------------------
        # LOW BATTERY CONDITION
        # ----------------------------------
        # Trigger alert if:
        # Battery <= 20%
        # AND charger is not connected
        if percent <= LOW_BATTERY and not plugged:

            # Send notification only once
            if last_alert != "low":

                show_notification(
                    "Low Battery Warning ⚠️",
                    f"Battery is at {percent}%. Please charge your device."
                )
                # Remember last alert sent
                last_alert = "low"
        # ----------------------------------
        # FULL BATTERY CONDITION
        # ----------------------------------
        # Trigger alert if:
        # Battery is 100%
        # AND charger is connected
        elif percent >= FULL_BATTERY and plugged:
            # Send notification only once
            if last_alert != "full":

                show_notification(
                    "Battery Full 🔋",
                    "Your battery is fully charged. You can unplug the charger."
                )

                # Remember last alert sent
                last_alert = "full"
        # ----------------------------------
        # RESET LOW/FULL ALERT STATUS
        # ----------------------------------
        # Charger connected but battery not yet full
        # Reset alert so full notification can appear later
        elif plugged and percent < FULL_BATTERY:
            last_alert = None
        # Charger disconnected and battery above low level
        # Reset alert so low notification can appear later
        elif not plugged and percent > LOW_BATTERY:
            last_alert = None
        # Wait before checking battery again
        time.sleep(CHECK_INTERVAL)
# ----------------------------
# Program Entry Point
# ----------------------------
# Runs only when this file is executed directly
if __name__ == "__main__":
    main()





 