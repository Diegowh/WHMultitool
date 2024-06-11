"""
Module responsible for the entire configuration of the application.
"""


from dataclasses import dataclass, field
from typing import Dict, List
from src.config.service_config import ServiceConfig
from src.config.exceptions import ConfigError
from src.utils.utils import get_version

# Screen
_version = get_version()
APP_VERSION = f"v{_version}"
APP_NAME = "All in One"
APP_WIDTH = 400
APP_HEIGHT = 350
APP_TITLE = f"ADAT - {APP_NAME}"

# Services
SERVICES = {
    "AutoSim": "Auto-Sim",
    "AutoEggDrop": "Auto-Eggdrop",
    "BabyFeeder": "Baby Feeder",
    "AutoFarm": "Auto-Farm",
    "MagicF": "Magic-F"
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
    "Veggies Mode": "veggies",
    "Honey Mode": "honey",
    "Sap Mode": "sap",
    "Paste Mode": "pas",
    "Dumper": "dumper",
    "Crafter": "crafter"
}

# Main Loop
MAIN_LOOP_SLEEP_INTERVAL = 0.05
DELETE_WINDOW_PROTOCOL = "WM_DELETE_WINDOW"
OPTION_PATTERN = "*tearOff"
ARK_ASCENDED_WINDOW_TITLE = "ArkAscended"


def load_service(service_name: str) -> ServiceConfig | None:
    """Load the configuration of a service.

    Args:
        service_name (str): Name of the service to load.

    Returns:
        ServiceConfig | None: ServiceConfig object
        if the service was loaded successfully.
        None otherwise.
    """
    try:
        return ServiceConfig(service_name)
    except ConfigError as e:
        print(e)
        return None


@dataclass(frozen=False)
class Config:

    app_version: str = APP_VERSION
    app_name: str = APP_NAME
    app_width: int = APP_WIDTH
    app_height: int = APP_HEIGHT
    app_title: str = APP_TITLE

    services: Dict[str, str] = field(default_factory=lambda: SERVICES)
    foods: List[str] = field(default_factory=lambda: FOODS)
    food_keywords: Dict[str, str] = field(default_factory=lambda: FOOD_KEYWORDS)

    # Main loop
    main_loop_sleep_interval: float = MAIN_LOOP_SLEEP_INTERVAL
    delete_window_protocol: str = DELETE_WINDOW_PROTOCOL
    option_pattern: str = OPTION_PATTERN

    # Magic F
    magic_f_options: Dict[str, str] = field(default_factory=lambda: MAGIC_F_OPTIONS)
