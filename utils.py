import pyautogui


def get_screen_resolution()->tuple[int, int]:
    resolution = pyautogui.size()
    return resolution.width, resolution.height