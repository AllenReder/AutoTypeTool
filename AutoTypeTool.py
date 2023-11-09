import pyautogui
import time

def autoType(text, interval, delay):
    """
    Auto type text.
    Args:
        text: text to type
        interval: interval between each character
        delay: delay before typing
    """
    time.sleep(delay)
    pyautogui.typewrite(text, interval=0)