import json


default_config = {
    "APP_VERSION": "v - default",
    "AUTOSIM_KEY": "f1",
    "APP_WEIGHT": 300,
    "APP_HEIGHT": 200,
    "APP_TITLE": "ADAT - AutoSim",
    "BACKGROUND_IMAGE": "messi_en_brazos.jpg",
}

class ConfigError(Exception):
    pass

class Config:
    def __init__(self) -> None:
        
        self.config = None
        self._load_config()

        if self.config is None:
            raise ConfigError("Failed to load configuration.")
        
        for key in self.config:
            setattr(self, key, self.config[key])


    def _load_config(self) -> None:
        try:
            with open("config.json", "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            with open("config.json", "w") as f:
                json.dump(default_config, f, indent=4)
                print("Could not find config.json, created a new one with default values.")
