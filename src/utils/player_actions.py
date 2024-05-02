import time
import keyboard
from enum import StrEnum
import pyperclip
import pyautogui
from src.utils.utils import get_screen_resolution
from src.utils.screen_manager import ScreenCoordsEnum

class MoveDirection(StrEnum):
    FORWARD = 'w'
    BACKWARD = 's'
    LEFT = 'a'
    RIGHT = 'd'


def lay_down(
    prev_delay: float = None, 
    post_delay: float = 0.2
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('x')
    time.sleep(post_delay)

def teleport_to_default(
    prev_delay: float = None, 
    post_delay: float = 1.5
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('r')
    time.sleep(post_delay)

def jump(
    prev_delay: float = None, 
    post_delay: float = 0.2
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('space')
    time.sleep(post_delay)

def pop_item(
    prev_delay: float = None, 
    post_delay: float = 0.2
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('o')
    time.sleep(post_delay)

def move(
    direction: MoveDirection, 
    prev_delay: float = None,
    duration: float = 0.2
    ) -> None:
    
    if not isinstance(direction, MoveDirection):
        raise ValueError(f'The direction must be an instance of {MoveDirection.__name__}')
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    keyboard.press(direction)
    time.sleep(duration)
    keyboard.release(direction)

def open_inventory(
    prev_delay: float = None, 
    post_delay: float = 0.2
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('i')
    time.sleep(post_delay)

def close_inventory(
    prev_delay: float = None, 
    post_delay: float = 0.2
    ) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    keyboard.press_and_release('esc')
    time.sleep(post_delay
)
def move_cursor(
    location: ScreenCoordsEnum,
    prev_delay: float = None,
    post_delay: float = None,
) -> None:
    
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    screen_w, screen_h = get_screen_resolution()
    
    # Convert relative coords to absolute coords
    x = location.value[0] * screen_w
    y = location.value[1] * screen_h
    
    # Move the cursor to the location
    pyautogui.moveTo(x, y)
    
    if post_delay is not None:
        time.sleep(post_delay)
    

def move_cursor_and_click(
    location: ScreenCoordsEnum,
    prev_delay: float = None,
    post_delay: float = 0.2,
    clicks: int = 1
    
) -> None:
    move_cursor(
        location=location, 
        prev_delay=prev_delay
    )
    
    pyautogui.click(clicks=clicks)
    print(f"Clicked")
    time.sleep(post_delay)
    
def type_text(
    text: str,
    prev_delay: float = None,
    post_delay: float = 0.2
) -> None:
    if prev_delay is not None:
        time.sleep(prev_delay)
    
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(post_delay)