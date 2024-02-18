import time

import pyautogui

# To use this script, Run it and go to you telegram web app
# Click on the Message area. and leave it :)

time.sleep(10)
for i in range(51):
    for c in f"Hello Houssam from automated script {i}":
        pyautogui.press(c)
    pyautogui.click()
    pyautogui.press("Enter")
    time.sleep(5)
