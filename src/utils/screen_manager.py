# This module serves as a tool for obtaining
# relative screen coordinates to create more enums as needed
# for the different services of the application.
# It can be run directly, and it will call the function get_mouse_relative_position()
# responsible for obtaining the relative position of the mouse
# on the screen based on the screen resolution.
# This way it is easier to create new enums for the different services
# of the application.
"""
This module contains functions, classes, and enums
responsible for obtaining and managing screen coordinates.
"""

__all__ = [
    "PlayerInventoryCoordinates",
    "StructureInventoryCoordinates",
    "MainMenuScreenCoordinates",
    "GameModeScreenCoordinates",
    "ServerSelectionScreenCoordinates",
    "ModsSelectionScreenCoordinates",
    "relative_position",
    "get_screen_resolution",
]


import time
from enum import Enum
import pyautogui


class ScreenCoordsEnum(Enum):
    """
    Enum class used to store relative screen coordinates.
    """


class PlayerInventoryCoordinates(ScreenCoordsEnum):
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
    SLOT1 = (0.116, 0.262)
    SLOT2 = (0.163, 0.265)
    SLOT3 = (0.212, 0.266)
    SLOT7 = (0.114, 0.351)
    SLOT8 = (0.164, 0.351)
    SLOT9 = (0.212, 0.354)
    CLOSE = (0.937, 0.06)


class StructureInventoryCoordinates(ScreenCoordsEnum):
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
    CLOSE = (0.937, 0.06)
    SLOT1= (0.465, 0.497)
    SLOT2= (0.698, 0.264)
    SLOT3= (0.746, 0.267)
    SLOT7= (0.65, 0.348)
    SLOT8= (0.699, 0.349)
    SLOT9= (0.749, 0.347)


class MainMenuScreenCoordinates(ScreenCoordsEnum):
    """
    This class is used to store the relative screen coordinates of the main menu screen.
    """
    PRESS_TO_START = (0.49, 0.79)
    JOIN_LAST_SESSION = (0.49, 0.88)
    ESC = (0.92, 0.095)


class GameModeScreenCoordinates(ScreenCoordsEnum):
    """
    This class is used to store the relative screen coordinates of the game mode screen.
    """
    BOBS_TALL_TALES = (0.055, 0.555)
    JOIN_GAME = (0.314, 0.533)
    CREATE_OR_RESUME_GAME = (0.541, 0.544)
    MODS_LIST = (0.76, 0.521)
    BACK = (0.499, 0.893)

class ServerSelectionScreenCoordinates(ScreenCoordsEnum):
    """
    This class is used to store the relative screen coordinates of the server selection screen.
    """
    FIRST_SERVER = (0.502, 0.305)
    SEARCH_BOX = (0.834, 0.179)
    ESC = (0.922, 0.097)
    BACK = (0.087, 0.817)
    REFRESH = (0.501, 0.869)
    JOIN = (0.893, 0.878)


class ModsSelectionScreenCoordinates(ScreenCoordsEnum):
    """
    This class is used to store the relative screen coordinates of the mods selection screen.
    """
    JOIN = (0.18, 0.866)
    BACK = (0.285, 0.865)


class ConnectionFailedScreenCoordinates(ScreenCoordsEnum):
    """
    This class is used to store the relative screen coordinates of the connection failed screen.
    """
    ACCEPT = (0.443, 0.676)
    CANCEL = (0.558, 0.676)
    
def relative_position(abs_position: tuple, screen_res: tuple) -> tuple[float, float]:
    """
    This function converts absolute screen coordinates to relative screen coordinates.
    """
    assert len(abs_position) == 2, "The absolute position must be a tuple of length 2."
    assert len(screen_res) == 2, "The screen resolution must be a tuple of length 2."
    return round(abs_position[0] / screen_res[0], 3), round(abs_position[1] / screen_res[1], 3)


def get_screen_resolution() -> tuple[int, int]:
    """
    This function returns the screen resolution of the monitor.
    """
    return (pyautogui.size().width, pyautogui.size().height)


def get_mouse_relative_position() -> tuple[int, int]:
    """Get the relative position of the mouse on the screen. Based on the screen resolution.

    Returns:
        tuple[int, int]: The relative position of the mouse on the screen.
    """
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
