import time
import pyautogui
from datetime import datetime

# Optional safety feature - add a pause after each action
pyautogui.PAUSE = 0.5

# Failsafe - quickly move mouse to upper-left corner to abort
pyautogui.FAILSAFE = False

def wait_until_time(minutes):
    target_time = time.time() + (minutes * 60)
    
    while time.time() < target_time:
        remaining = int(target_time - time.time())
        print(f"Time remaining: {remaining//60}:{remaining%60:02d}", end='\r')
        time.sleep(20)
    print("\nTime's up!")

def perform_actions():
    # Press alt+tab
    try:
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('alt')
        time.sleep(0.2)  # Hold the keys briefly
    finally:
        # Make sure to release all keys even if something goes wrong
        pyautogui.keyUp('alt')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    time.sleep(2)  # Wait for window switch

    pyautogui.hotkey('alt', 'tab')
    time.sleep(3)  # Wait for window switch
    
    # Click location A
    pyautogui.click(x=77, y=116)  # end session
    time.sleep(1)  
    
    # Click location B
    pyautogui.click(x=22, y=37)  # go back
    time.sleep(1)  
    
    pyautogui.moveTo(500, 500)  # Move mouse to a neutral location, so the scroll works
    time.sleep(1)  
    # Scroll down 20 lines
    pyautogui.scroll(-1500)  # Negative number scrolls down
    time.sleep(1)  # Wait for scroll to complete
    
    # Click location C
    pyautogui.click(x=949, y=982)  # start new session
    time.sleep(1)  
    pyautogui.hotkey('alt', 'tab')

def main():
    # print("Script starting...")
    # print("Move mouse to upper-left corner to abort")
    # print("You have 5 seconds to switch to your target application...")
    
    # # Initial wait for setup
    # time.sleep(10)
    
    # # Get the coordinates for each location
    # print("To get coordinates for each location:")
    # input("Press Enter when ready to capture location A...")
    # pos_a = pyautogui.position()
    # print(f"Location A: {pos_a}")
    
    # input("Press Enter when ready to capture location B...")
    # pos_b = pyautogui.position()
    # print(f"Location B: {pos_b}")
    
    # input("Press Enter when ready to capture location C...")
    # pos_c = pyautogui.position()
    # print(f"Location C: {pos_c}")
    
    # print("\nCoordinates captured. Update the script with these values.")
    # print("Starting 13 minute timer...")
    
    while True:
        wait_until_time(13)
    
        perform_actions()
if __name__ == "__main__":
    main()