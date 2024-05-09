from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop
from src.controllers.magic_f import MagicF
from src.controllers.sub.mf_feed import MFFeed
from src.controllers.sub.mf_retrieve import MFRetrieve
from src.controllers.sub.mf_keep_only import MFKeepOnly


# Private settings for the application

# Screen
APP_VERSION = "v1.0"
APP_NAME = "All in One"
APP_WEIGHT = 400
APP_HEIGHT = 500
APP_TITLE = f"{APP_VERSION} - ADAT - {APP_NAME}"



# Services
SERVICES = {
    "AutoSim": AutoSim,
    "AutoEggDrop": AutoEggDrop,
    "Magic-F": MagicF,
}

MAGIC_F_SUBSERVICES = {
    "KeepOnly": MFKeepOnly,
    "AutoFeed": MFFeed,
    "Retrieve": MFRetrieve,
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

# Main Loop
MAIN_LOOP_SLEEP_INTERVAL = 0.05
DELETE_WINDOW_PROTOCOL = "WM_DELETE_WINDOW"
OPTION_PATTERN = "*tearOff"