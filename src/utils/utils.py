"""
Module to handle utility functions, not enough related to be in a separate module.
"""


import pyautogui
import pyperclip


def dummy_routine():
    """Routine to test the functionality of the service.
    """
    print("INICIADA RUTINA!!")
    # pyautogui.PAUSE = 0.5
    # pyautogui.typewrite("fert", interval=0.0)
    text = "fert"
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    print("TERMINADA RUTINA!!")
