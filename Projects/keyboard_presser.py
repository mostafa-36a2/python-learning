# import time

# import pyautogui

# # To use this script, Run it and go to you telegram web app
# # Click on the Message area. and leave it :)

# time.sleep(5)
# for i in range(51):
#     for (
#         c
#     ) in f"h.f.j.f.G.h.f.k.j.h.G.f.d.h.f.j.f.G.h.f.k.j.h.G.f.d.f.h.f.j.f.G.h.f.k.j.h.G.f.d.h.f.j.f.G.h.f.k.j.h.G.f.d.f.h.f.j.f.G.h.f.k.j.h.G.f.d.h.f.j.f.G.h.f.k.j.h.G.f.d.f.h.f.j.f.G.h.f.k.j.h.G.f.d.h.f.j.f.G.h.f.k.j.h.G.f.d.f":
#         pyautogui.press(c)
#     pyautogui.click()

#     pyautogui.press("Enter")
#     time.sleep(5)

import re


def __validate_db_name(value) -> bool:
    """
    >>> __validate_db_name("test")
    True
    >>> __validate_db_name("test12")
    True
    >>> __validate_db_name("sql -- injection")
    False
    >>> __validate_db_name("test.test")
    False
    >>> __validate_db_name("test.test")
    False
    """
    return bool(re.match("^[^0-9][a-zA-Z0-9_]{2,62}$", value))
