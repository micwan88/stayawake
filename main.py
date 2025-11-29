import pyautogui
import time

SLEEP_TIME_IN_SEC = 10
# shift / esc ? - just trying to use any key press which will not affect any application
TARGET_KEYBOARD_BUTTON = r'esc'

def main():
    # Turn off failsafe, otherwise, sometimes program will throw error when moving mouse cursor
    pyautogui.FAILSAFE = False

    print("Mouse Jiggler starting ... (Ctrl + C to stop)")

    try:
        while True:
            # move cursor to right : 1 pixel
            pyautogui.moveRel(1, 0)
            
            # sleep for a while and let computer detect your movement
            time.sleep(0.5)
            
            # move back cursor : 1 pixel
            pyautogui.moveRel(-1, 0)

            # Teams "status" seems depends on keyboard
            pyautogui.press(TARGET_KEYBOARD_BUTTON)
            
            # Output console, just to make sure the program is running
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"[{current_time}] Mouse move and key press executed")

            # sleep for a while
            time.sleep(SLEEP_TIME_IN_SEC)
    except KeyboardInterrupt:
        print("Program Stop")

if __name__ == "__main__":
    main()
