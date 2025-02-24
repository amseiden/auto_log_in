import time
import pyautogui
import pyperclip
import subprocess


def activate_application(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")


def click_and_paste(x, y, text):
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.typewrite(pyperclip.paste())
    time.sleep(0.2)
    pyautogui.press('enter')


def main():
    app_name = "Cisco AnyConnect Secure Mobility Client"
    activate_application(app_name)

    pyautogui.click(465, 180)
    time.sleep(3)

    # Insert your EMAIL
    click_and_paste(570, 290, "INSEER_YOUR_EMAIL")
    time.sleep(1)

    # Insert your PASSWORD then follow the steps from help.txt
    click_and_paste(574, 347, "INSEER_YOUR_PASSSWOER")
    time.sleep(1)

    pyautogui.press('enter')


if __name__ == "__main__":
    main()
