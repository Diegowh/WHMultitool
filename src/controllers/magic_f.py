import asyncio
from typing import TYPE_CHECKING

from src.components.windows.magic_f_gui import MagicFGUI
if TYPE_CHECKING:
    from config.config import Config

class MagicF:
    
    def __init__(self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller,
    ):
        self.loop = loop
        self.app_config = config
        self.gui = MagicFGUI(
            magic_f=self,
            master=master,
            app_controller=app_controller
            
        )
    
    def __name__(self):
        for key, value in self.app_config.services.items():
           if value is MagicF:
               return key
        return None