import pyautogui
import pyperclip
from enum import StrEnum
from player_actions import *
import time
import asyncio

def get_screen_resolution()->tuple[int, int]:
    resolution = pyautogui.size()
    return resolution.width, resolution.height



class TaskName(StrEnum):
    pass

def dummy_routine():
    print("INICIADA RUTINA!!")
    # pyautogui.PAUSE = 0.5
    # pyautogui.typewrite("fert", interval=0.0)
    text = "fert"
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    print("TERMINADA RUTINA!!")