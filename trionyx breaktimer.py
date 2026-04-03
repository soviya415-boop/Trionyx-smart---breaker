import time
import datetime
import tkinter as tk
from tkinter import messagebox

def strfdelta(tdelta):
    """Formats the timedelta into a readable string."""
    seconds = int(tdelta.total_seconds())
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def alert_user():
    """Creates a simple pop-up window that stays on top."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tiny window
    root.attributes("-topmost", True)  # Make sure the pop-up appears on top
    messagebox.showinfo("Break Timer", "Time to step away from the screen!")
    root.destroy()

def start_break_timer():
    try:
        minutes = float(input("How many minutes between breaks? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    seconds_interval = int(minutes * 60)
    
    while True:
        target_time = time.time() + seconds_interval
        
        while time.time() < target_time:
            remaining_seconds = int(target_time - time.time())
            remaining_delta = datetime.timedelta(seconds=remaining_seconds)
            
            # Print countdown - works best in CMD/Terminal
            print(f"Time remaining until break: {strfdelta(remaining_delta)}", end="\r", flush=True)
            time.sleep(1)
        
        print("\n" + "="*30)
        print("TIME FOR A BREAK!")
        print("="*30)

        # Triggers the pop-up alert
        alert_user()

        ans = input("Press Enter to resume or type 'exit' to quit: ").lower()
        if 'exit' in ans:
            print("Timer stopped.")
            break
            
        print("Restarting timer...")

if __name__ == "__main__":
    start_break_timer()
