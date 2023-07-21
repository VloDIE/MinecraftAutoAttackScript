import flet as ft
from flet import *
from ahk import AHK
import time
import winsound
import threading

ahk = AHK()
ahk.set_capslock_state(0)


def clicker():
    while True:
        if ahk.key_state('CapsLock', mode='T') and ahk.key_state('alt', mode='P'):
            ahk.click()
            time.sleep(0.625)


def app(page: ft.page):
    page.title = 'AutoAttackScript'
    page.window_width = 460
    page.window_height = 620
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_activate(e):
        ahk.set_capslock_state()
        play_sounds()

    def for_hotkey():
        ahk.set_capslock_state()
        play_sounds()

    def play_sounds():
        if ahk.key_state('CapsLock', mode='T'):
            winsound.PlaySound('assets/sounds/on.wav', winsound.SND_FILENAME)
            activate_btn.text = "OFF"
        else:
            winsound.PlaySound('assets/sounds/off.wav', winsound.SND_FILENAME)
            activate_btn.text = "ON"
        page.update()

    def change_theme(e):
        if page.theme_mode == "DARK":
            page.theme_mode = "LIGHT"
            main_cont.gradient.colors = [ft.colors.WHITE, ft.colors.PURPLE]
            change_theme_btn.icon = ft.icons.BEDTIME
            logo.image_src = 'assets/images/light_theme/logo.png'
        else:
            page.theme_mode = "DARK"
            main_cont.gradient.colors = ['#7038aa', '#160033']
            logo.image_src = 'assets/images/dark_theme/logo.png'
            change_theme_btn.icon = ft.icons.WB_SUNNY_ROUNDED
        time.sleep(0.2)  # задержка чисто для красоты
        page.update()

    change_theme_btn = ft.IconButton(icon=ft.icons.BEDTIME,
                                     tooltip="Change appearance mode", on_click=change_theme,
                                     height=50, width=50)

    logo = ft.Container(
        width=350, height=400,
        image_src='assets/images/light_theme/logo.png',
        image_fit=ft.ImageFit.CONTAIN)

    activate_btn = ft.OutlinedButton(
        width=150, height=150, on_click=toggle_activate,
        text='ON' if ahk.key_state('CapsLock', mode='T') == 0 else 'OFF',
        style=ft.ButtonStyle(shape=ft.CircleBorder(),
                             side=BorderSide(3, color=ft.colors.PURPLE)))

    # x тут что-бы ошибки не-было
    support_btn = ft.TextButton(text="Поддержать",
                                on_click=lambda x: page.launch_url("https://www.donationalerts.com/r/vlodie"),
                                width=120, height=100, style=ft.ButtonStyle(color=ft.colors.WHITE,
                                                                            overlay_color=ft.colors.TRANSPARENT))

    # ft.colors.INDIGO
    main_cont = (ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.WHITE, ft.colors.PURPLE]),
        content=ft.Stack([
            ft.Container(
                alignment=ft.alignment.top_right,
                top=10, right=10,
                content=change_theme_btn),

            ft.Container(
                left=40,
                content=logo),

            ft.Container(
                top=280, left=130,
                width=200, height=200,
                padding=10,
                content=activate_btn),

            ft.Container(
                alignment=ft.alignment.bottom_left, left=3, bottom=10,
                width=120, height=100,
                content=support_btn
            )

        ]),
        width=460,
        height=620,
        margin=-10
    ))

    page.add(main_cont)
    page.update()

    ahk.add_hotkey("CapsLock", callback=for_hotkey)
    ahk.start_hotkeys()

    clicker_thread = threading.Thread(target=clicker())
    clicker_thread.start()


if __name__ == "__main__":
    ft.app(target=app)

# bg colors = light theme: ['#ffffff', 'ff00ff'], dark theme ['#7038aa', '#160033']
# icon colors = light theme #D235D2, dark theme #353358
