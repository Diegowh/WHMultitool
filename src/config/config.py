from src.config.service_config import ServiceConfig
from src.config.exceptions import ConfigError


class Config:
    def __init__(self) -> None:
        self.APP_VERSION = "v0.5.1"
        self.APP_WEIGHT = 350
        self.APP_HEIGHT = 200
        self.APP_TITLE = f"{self.APP_VERSION} - ADAT - All in One"

    def load_service(self, service_name: str) -> ServiceConfig | None:
        try:
            return ServiceConfig(service_name)
        except ConfigError as e:
            print(e)
            return None