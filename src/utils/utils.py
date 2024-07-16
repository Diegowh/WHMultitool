"""
Module to handle utility functions, not enough related to be in a separate module.
"""


import pyautogui
import pyperclip
import base64
import toml


def favicon_encoder():
    icon_path = "src/assets/favicon.ico"
    with open(icon_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Write the encoded string to a file
    with open("encoded_favicon.txt", "w") as text_file:
        text_file.write(encoded_string)

    return encoded_string


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


def transcript_attr_name(attr_name: str) -> str:
    assert isinstance(attr_name, str)
    attr_name = attr_name.replace("_", " ")
    return attr_name.title()


def get_version():
    try:
        pyproject = toml.load("pyproject.toml")
        version = pyproject.get("tool", {}).get("poetry", {}).get("version", "")

    except FileNotFoundError:
        return "1.8.4"

    return version
