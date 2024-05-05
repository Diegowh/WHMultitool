"""
Module for handling service configuration
"""
from configparser import ConfigParser
from src.config.exceptions import ConfigError

# __current_dir__ = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_NAME = "src/config/config.ini"
# __config_path__ = os.path.join(__current_dir__, CONFIG_FILE_NAME)

class ServiceConfig:
    """
    Configuration class for a service.
    """
    def __init__(self, service_name: str) -> None:
        # Try to read the .ini file
        self.config = ConfigParser()
        try:
            self.config.read(CONFIG_FILE_NAME)
        except FileNotFoundError as exc:
            raise ConfigError("config.ini was not found") from exc

        self.service_name = service_name
        self._load_config()

    def _load_config(self) -> None:
        print(self.config.sections())
        if self.service_name in self.config:
            for key in self.config[self.service_name]:
                setattr(self, key, self.config[self.service_name][key])
                print(f"{key}: {self.config[self.service_name][key]}")

    def update(self, attr_name: str, new_value: str) -> None:
        """Update the configuration of a service.

        Args:
            attr_name (str): The name of the attribute to update.
            new_value (str): The new value of the attribute.
        """
        if self.service_name in self.config and attr_name in self.config[self.service_name]:

            # update the configparser object
            self.config[self.service_name[attr_name]] = new_value

            # update the object attribute
            setattr(self, attr_name, new_value)
            with open(CONFIG_FILE_NAME, "w", encoding="utf-8") as f:
                self.config.write(f)
