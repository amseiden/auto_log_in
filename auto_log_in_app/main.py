import time
import pyautogui
import pyperclip
import subprocess


def activate_application(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        time.sleep(2)
    except Exception as e:
        print(f"Eroare la activarea aplicației: {e}")


def click_and_paste(x, y, text):
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyperclip.copy(text)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)


def click(x, y):
    pyautogui.click(x, y)
    time.sleep(2)


def main():
    app_name = "Cisco AnyConnect Secure Mobility Client"
    activate_application(app_name)

    # Prima secvență
    click(465,180)

    click_and_paste(570, 290, "X")

    # A doua secvență
    click_and_paste(574, 347, "X")

    click(848, 438)


if __name__ == "__main__":
    main()
