import asyncio
from typing import TYPE_CHECKING

from asyncio import AbstractEventLoop
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.sub.mf_feed_gui import MFFeedGUI
if TYPE_CHECKING:
    from config.config import Config
    from src.controllers.magic_f import MagicF

class MFFeed(BaseTaskManager):
    
    def __init__(
        self,
        loop: AbstractEventLoop,
        config: 'Config',
        master,
        mf_controller: 'MagicF'
        ) -> None:
        super().__init__(loop)
        
        self.app_config = config
        self.config = self.app_config.load_service(self.__name().upper())
        
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key)
        
        self.gui = MFFeedGUI(
            mf_feed=self,
            master=master,
            mf_controller=mf_controller
        )
        
    def __name__(self):
        for key, value in self.app_config.services.items():
           if value is MFFeed:
               return key
        return None
    
    async def _task(self):
        print("MFFeed task running")
        await asyncio.sleep(2)