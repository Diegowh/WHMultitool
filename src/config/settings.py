from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop
from src.controllers.babyfeeder import BabyFeeder
from src.controllers.autofarm import AutoFarm
from src.controllers.magic_f import MagicF

# Private settings for the application

# Screen

APP_VERSION = "v1.4.0"
APP_NAME = "All in One"
APP_WIDTH = 400
APP_HEIGHT = 350
APP_TITLE = f"ADAT - {APP_NAME}"



# Services
SERVICES = {
    "AutoSim": AutoSim,
    "AutoEggDrop": AutoEggDrop,
    "BabyFeeder": BabyFeeder,
    "AutoFarm": AutoFarm,
    "Magic-F": MagicF
}


# --- Magic-F --- #
# Feed
FOODS = [
    "Raw Meat",
    "Raw Fish",
    "Cooked Meat",
    "Berry",
    
]

FOOD_KEYWORDS = {
    "Raw Meat": "raw",
    "Raw Fish": "fish",
    "Cooked Meat": "cooked",
    "Berry": "berry",
}

MAGIC_F_OPTIONS = {
    "Paste Mode": "pas",
    "Sap Mode": "sap",
    "Honey Mode": "honey",
    "Veggies Mode": "veggies",
    "Dumper": "dumper",
    "Crafter": "crafter"
}

# Main Loop
MAIN_LOOP_SLEEP_INTERVAL = 0.05
DELETE_WINDOW_PROTOCOL = "WM_DELETE_WINDOW"
OPTION_PATTERN = "*tearOff"
ARK_ASCENDED_WINDOW_TITLE = "ArkAscended"