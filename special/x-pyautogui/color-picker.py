# pip install pynput
# https://stackoverflow.com/questions/39235454/how-to-know-if-the-left-mouse-click-is-pressed
# https://stackoverflow.com/questions/71487975/how-to-detect-the-colour-of-the-specific-pixel-the-mouse-curser-is-directly-on

from pynput import mouse

import pyautogui


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        px = pyautogui.pixel(x, y)
        if pressed == True:
            print(px)
        # return (
        #    False  # Returning False if you need to stop the program when Left clicked.
        # )
    else:
        return False


listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
