from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop
from src.controllers.babyfeeder import BabyFeeder
from src.controllers.sub.mf_retrieve import MFRetrieve
from src.controllers.sub.mf_keep_only import MFKeepOnly
from src.controllers.autofarm import AutoFarm

# Private settings for the application

# Screen

APP_VERSION = "v1.2.6"
APP_NAME = "All in One"
APP_WEIGHT = 300
APP_HEIGHT = 320
APP_TITLE = f"ADAT - {APP_NAME}"



# Services
SERVICES = {
    "AutoSim": AutoSim,
    # "Magic-F": MagicF,
    "AutoEggDrop": AutoEggDrop,
    "BabyFeeder": BabyFeeder,
    "AutoFarm": AutoFarm,
}

MAGIC_F_SUBSERVICES = {
    "KeepOnly": MFKeepOnly,
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

# Keep Only
KEEP_ONLY_ITEMS = [
    "Metal",
    "Stone",
    "Wood",
    "MejoBerry",
    "TintoBerry",
    "NarcoBerry",
    # "Raw Meat",
    # "Raw Fish",
    # "Cooked Meat",
    # "Berry",
    "StimBerry",
    # "Honey",
    # "Sap",
    # "Paste"
    # "Veggies",
]

KEEP_ONLY_ITEM_SEQUENCE = {
    "MejoBerry": ["v", "a", "t"],
    "StimBerry": ["o", "a", "v"],
    "TintoBerry": ["a", "v", "m"],
    "NarcoBerry": ["v", "m", "z", "i"],
    "Stone": ["a", "w", "f"],
    "Metal": ["n", "c", "w"],
    "Wood": ["t", "e"]
}
# Main Loop
MAIN_LOOP_SLEEP_INTERVAL = 0.05
DELETE_WINDOW_PROTOCOL = "WM_DELETE_WINDOW"
OPTION_PATTERN = "*tearOff"
ARK_ASCENDED_WINDOW_TITLE = "ArkAscended"