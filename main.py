import keyboard
import time
from ctypes import windll
import mouse

active = False


def toggle_variable():
    global active
    active = not active


keyboard.add_hotkey('alt', toggle_variable)


def main():
    while windll.user32.GetAsyncKeyState(0x01) > 0 and active:
        print(windll.user32.GetAsyncKeyState(0x01))
        time.sleep(0.625)
        mouse.click(button='left')


while True:
    main()
