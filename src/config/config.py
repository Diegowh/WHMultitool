"""
Module responsible of the entire configuration of the application.
"""


from src.config.service_config import ServiceConfig
from src.config.exceptions import ConfigError
from src.config.settings import *


class Config:
    """Main configuration class of the application.
    """
    def __init__(self) -> None:
        self.app_version = APP_VERSION
        self.app_name = APP_NAME
        self.app_width = APP_WIDTH
        self.app_height = APP_HEIGHT
        self.app_title = APP_TITLE


        self.services = SERVICES
        self.foods = FOODS
        self.food_keywords = FOOD_KEYWORDS


        # Main loop
        self.main_loop_sleep_interval = MAIN_LOOP_SLEEP_INTERVAL
        self.detele_window_protocol = DELETE_WINDOW_PROTOCOL
        self.option_pattern = OPTION_PATTERN
        
        # Magic F
        self.magic_f_options = MAGIC_F_OPTIONS

    def load_service(self, service_name: str) -> ServiceConfig | None:
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
