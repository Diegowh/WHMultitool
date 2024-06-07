"""
Module to handle player actions in the game.
"""


import asyncio
import time
from enum import StrEnum
import keyboard
import pyperclip
import pyautogui

from src.utils.screen_manager import (
    ScreenCoordsEnum,
    get_screen_resolution,
)
from src.utils.validators import validate_hotkey


class MoveDirection(StrEnum):
    """
    Enum to represent the directions in which the player can moved in the game.
    """
    FORWARD = 'w'
    BACKWARD = 's'
    LEFT = 'a'
    RIGHT = 'd'


@validate_hotkey
async def lay_down(
    hotkey: str = 'x',
    pre_delay: float = None,
    post_delay: float = 0.2,
    ) -> None:
    """Lay down the player in the game.

    Args:
        hotkey (str, optional): Keybind to lay down the player. Defaults to 'x'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def teleport_to_default(
    hotkey: str = 'r',
    pre_delay: float = None,
    post_delay: float = 1.5
    ) -> None:
    """Teleport the player to the set default location.

    Args:
        hotkey (str, optional): Keybind to use default teleport. Defaults to 'r'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 1.5.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def jump(
    hotkey: str = 'space',
    pre_delay: float = None,
    post_delay: float = 0.2
    ) -> None:
    """Make the player jump in the game.

    Args:
        hotkey (str, optional): Keybind to jump in game. Defaults to 'space'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)
    
    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def craft_all(
    hotkey: str = 'a',
    pre_delay: float = None,
    post_delay: float = 0.2
    ) -> None:
    
    if pre_delay is not None:
        time.sleep(pre_delay)
    
    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def pop_item(
    hotkey: str = 'o',
    pre_delay: float = None,
    post_delay: float = 0.2
    ) -> None:
    """Pop an item from the inventory.

    Args:
        hotkey (str, optional): Keybind to pop an item in game. Defaults to 'o'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def move(
    direction: MoveDirection | str,
    pre_delay: float = None,
    duration: float = 0.2,
    post_delay: float = 0
    ) -> None:
    """Move the player in the game in a specific direction.

    Args:
        direction (MoveDirection): Direction in which the player will move.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.

    Raises:
        ValueError: If the direction is not an instance of MoveDirection.
    """

    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press(direction)
    time.sleep(duration)
    keyboard.release(direction)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def open_inventory(
    hotkey: str = 'i',
    pre_delay: float = None,
    post_delay: float = 0.2
    ) -> None:
    """Open the inventory in the game.

    Args:
        hotkey (str, optional): Keybind to open the inventory in game. Defaults to 'i'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


@validate_hotkey
async def close_inventory(
    hotkey: str = 'esc',
    pre_delay: float = None,
    post_delay: float = 0.2
    ) -> None:
    """Close the inventory in the game.

    Args:
        hotkey (str, optional): Keybind to close the inventory in game. Defaults to 'esc'.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press_and_release(hotkey)
    await asyncio.sleep(post_delay)


def move_cursor(
    location: ScreenCoordsEnum,
    pre_delay: float = None,
    post_delay: float = None,
) -> None:
    """Move the cursor to a specific location on the screen.

    Args:
        location (ScreenCoordsEnum): Enum representing the location on the screen.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to None.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    screen_w, screen_h = get_screen_resolution()

    # Convert relative coords to absolute coords
    x = location.value[0] * screen_w
    y = location.value[1] * screen_h

    # Move the cursor to the location
    pyautogui.moveTo(x, y)

    if post_delay is not None:
        time.sleep(post_delay)


async def move_cursor_and_click(
    location: ScreenCoordsEnum,
    pre_delay: float = None,
    post_delay: float = 0.2,
    clicks: int = 1
) -> None:
    """Move the cursor to a specific location on the screen and click.

    Args:
        location (ScreenCoordsEnum): Enum representing the location on the screen.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
        clicks (int, optional): Number of clicks to perform. Defaults to 1.
    """
    move_cursor(
        location=location,
        pre_delay=pre_delay
    )

    pyautogui.click(clicks=clicks)
    await asyncio.sleep(post_delay)


async def type_text(
    text: str,
    pre_delay: float = None,
    post_delay: float = 0.2
) -> None:
    """Type text into the game.

    Args:
        text (str): Text to type into the game.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    # I decided to use copy and paste instead of pyautogui.write because
    # it's more reliable and faster when typing long texts in ARK.
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    await asyncio.sleep(post_delay)


@validate_hotkey
async def key_down(
    key: str,
    pre_delay: float = None,
    post_delay: float = 0.2
) -> None:
    """Press a key down.

    Args:
        key (str): Key to press down.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.press(key)
    await asyncio.sleep(post_delay)
    
    
@validate_hotkey
async def key_up(
    key: str,
    pre_delay: float = None,
    post_delay: float = 0.2
) -> None:
    """Release a key.

    Args:
        key (str): Key to release.
        pre_delay (float, optional): Previous delay before executing the action. Defaults to None.
        post_delay (float, optional): Posterior delay after executing the action. Defaults to 0.2.
    """
    if pre_delay is not None:
        time.sleep(pre_delay)

    keyboard.release(key)
    await asyncio.sleep(post_delay)