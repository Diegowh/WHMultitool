"""
Module to store all the validator used in the application.
"""


from functools import wraps
import keyboard


class InvalidKeyError(Exception):
    """
    Exception raised for invalid hotkeys.
    """


def validate_hotkey(func):
    """Decorator to validate the hotkey argument.

    Args:
        func (function): Function to decorate.

    Raises:
        InvalidKeyError: If the hotkey is not a valid hotkey.

    Returns:
        function: Decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        hotkey = kwargs.get('hotkey')
        if hotkey is not None:
            try:
                keyboard.parse_hotkey(hotkey)
            except Exception:
                raise InvalidKeyError(f" '{hotkey}' is not a valid hotkey") from Exception
        return func(*args, **kwargs)
    return wrapper


def validate_map_number(input_str: str) -> bool:
    return input_str.isdigit() and len(input_str) <= 4 or input_str == ""
    