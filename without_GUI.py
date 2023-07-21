from ahk import AHK
import time
import winsound

ahk = AHK()
ahk.set_capslock_state(0)


def toggler():
    ahk.set_capslock_state()
    if ahk.key_state('CapsLock', mode='T'):
        print('script activate!')
        winsound.PlaySound('assets/sounds/on.wav', winsound.SND_FILENAME)
    else:
        print('script deactivate!')
        winsound.PlaySound('assets/sounds/off.wav', winsound.SND_FILENAME)


ahk.add_hotkey("CapsLock", callback=toggler)
ahk.start_hotkeys()


def clicker():
    while True:
        if ahk.key_state('CapsLock', mode='T') and ahk.key_state('alt', mode='P'):
            ahk.click()
            time.sleep(0.625)
            print('click!')

while True:
    clicker()
