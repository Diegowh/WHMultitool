from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop

# Private settings for the application

# Screen
APP_VERSION = "v0.11"
APP_NAME = "All in One"
APP_WEIGHT = 400
APP_HEIGHT = 500
APP_TITLE = f"{APP_VERSION} - ADAT - {APP_NAME}"



# Services
SERVICES = {
    "AutoSim": AutoSim,
    "AutoEggDrop": AutoEggDrop,
}



# Main Loop
MAIN_LOOP_SLEEP_INTERVAL = 0.05
DELETE_WINDOW_PROTOCOL = "WM_DELETE_WINDOW"
OPTION_PATTERN = "*tearOff"