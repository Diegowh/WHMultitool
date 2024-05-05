"""
Module responsible of the entire configuration of the application.

It is a centralized place to store all the configuration of the application
and load the configuration of the services.

Author: Diego WH
Date: 5/2024
"""
from src.config.service_config import ServiceConfig
from src.config.exceptions import ConfigError


class Config:
    """Main configuration class of the application.
    """
    def __init__(self) -> None:
        self.app_version = "v0.6.1"
        self.app_weight = 350
        self.app_height = 200
        self.app_title = f"{self.app_version} - ADAT - All in One"


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
