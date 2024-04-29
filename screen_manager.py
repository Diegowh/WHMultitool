"""
This module is used to store the conversion of absolute screen coordinates to relative screen coordinates.
"""

import pyautogui
from enum import Enum
import time


def relative_position(abs_position: tuple, screen_res: tuple) -> tuple[float, float]:
    """
    This function converts absolute screen coordinates to relative screen coordinates.
    """
    assert len(abs_position) == 2, "The absolute position must be a tuple of length 2."
    assert len(screen_res) == 2, "The screen resolution must be a tuple of length 2."
    
    return round(abs_position[0] / screen_res[0], 3), round(abs_position[1] / screen_res[1], 3)

class ScreenCoordinates(Enum):
    pass


class PlayerInventoryCoordinates(ScreenCoordinates):
    """
    This class is used to store the relative screen coordinates of the player's inventory.
    """
    SEARCH_BAR = (0.13, 0.18)
    TRANSFER_ALL = (0.18, 0.18)
    DROP_ALL = (0.21, 0.18)
    SORT_BY = (0.23, 0.18)
    NEW_FOLDER = (0.26, 0.18)
    AUTO_STACK = (0.28, 0.18)
    CUSTOM_COSMETIC = (0.31, 0.18)
    FOLDER_VIEW = (0.33, 0.18)
    TOGGLE_TOOLTIPS = (0.36, 0.18)
    FIRST_SLOT = (0.11, 0.26)


class StructureInventoryCoordinates(ScreenCoordinates):
    """
    This class is used to store the relative screen coordinates of the structure's inventory.
    """
    SEARCH_BAR = (0.66, 0.18)
    TRANSFER_ALL = (0.71, 0.18)
    DROP_ALL = (0.74, 0.18)
    SORT_BY = (0.77, 0.18)
    NEW_FOLDER = (0.79, 0.18)
    AUTO_STACK = (0.82, 0.18)
    CUSTOM_COSMETIC = (0.85, 0.18)
    FOLDER_VIEW = (0.87, 0.18)
    SHOW_ENGRAMS = (0.90, 0.18)
    YOU_BUTTON = (0.41, 0.13)
    STRUCTURE_BUTTON = (0.58, 0.13)
    
    

def get_screen_resolution() -> tuple[int, int]:
    """
    This function returns the screen resolution of the monitor.
    """
    return (pyautogui.size().width, pyautogui.size().height)

def get_mouse_relative_position() -> tuple[int, int]:
    screen_resolution = get_screen_resolution()
    while True:
        # Get the position of the mouse.
        position = pyautogui.position()
        x = position.x
        y = position.y
        
        absolute_coords = (x, y)
        relative_coords = relative_position(absolute_coords, screen_resolution)
        print(relative_coords)
        time.sleep(1)

if __name__ == "__main__":
    get_mouse_relative_position()