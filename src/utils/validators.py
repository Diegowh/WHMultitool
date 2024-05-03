import keyboard
from functools import wraps

class InvalidKeyError(Exception):
    pass


def validate_hotkey(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hotkey = kwargs.get('hotkey')
        if hotkey is not None:
            try:
                keyboard.parse_hotkey(hotkey)
            except Exception:
                raise InvalidKeyError(f" '{hotkey}' is not a valid hotkey")
        return func(*args, **kwargs)
    return wrapper