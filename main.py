import keyboard
import time
from ctypes import windll
import mouse
import winsound

active = False


def toggle_variable():
    global active
    active = not active
    if active:
        winsound.PlaySound('sounds/on.wav', winsound.SND_FILENAME)
    else:
        winsound.PlaySound('sounds/off.wav', winsound.SND_FILENAME)


keyboard.add_hotkey('alt', toggle_variable)


def main():
    while windll.user32.GetAsyncKeyState(0x05) > 0 and active:
        print(windll.user32.GetAsyncKeyState(0x05))
        time.sleep(0.625)
        mouse.click(button='left')


while True:
    main()
