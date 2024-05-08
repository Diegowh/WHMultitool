"""
Module responsible of the entire configuration of the application.
"""


from src.config.service_config import ServiceConfig
from src.config.exceptions import ConfigError
from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop


class Config:
    """Main configuration class of the application.
    """
    def __init__(self) -> None:
        self.app_version = "v0.7"
        self.app_weight = 400
        self.app_height = 500
        self.app_title = f"{self.app_version} - ADAT - All in One"

        self.main_loop_sleep_interval = 0.05

        self.services = {
            "AutoSim": AutoSim,
            "AutoEggDrop": AutoEggDrop,
        }

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
