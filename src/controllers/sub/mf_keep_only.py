import asyncio
from typing import TYPE_CHECKING
from asyncio import AbstractEventLoop
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.sub.mf_keep_only_gui import MFKeepOnlyGUI

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from config.config import Config
    from src.controllers.magic_f import MagicF

class MFKeepOnly(BaseTaskManager):
    
    def __init__(
        self,
        loop: 'AbstractEventLoop',
        config: 'Config',
        master,
        mf_controller: 'MagicF',
    ):
        super().__init__(loop, repetitive_task=False)
        
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key)
        
        self.gui = MFKeepOnlyGUI(
            mf_keep_only=self,
            master=master,
            mf_controller=mf_controller
        )
        
    def __name__(self):
        for key, value in self.app_config.magic_f_subservices.items():
           if value is MFKeepOnly:
               return key
        return None

    async def _task(self):
        print("MFKeepOnly task ran once")
        await asyncio.sleep(2)
        print("Second MFKeepOnly task ran")
        await asyncio.sleep(0)