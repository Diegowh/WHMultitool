from src.controllers.base_task_manager import BaseTaskManager
from typing import TYPE_CHECKING
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    StructureInventoryCoordinates,
    PlayerInventoryCoordinates
)
from src.components.windows.magic_f_gui import MagicFGUI

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from config.config import Config
    from src.controllers.app_controller import AppController

class MagicF(BaseTaskManager):
    

    def __init__(
        self,
        loop: 'AbstractEventLoop',
        config: 'Config',
        master,
        app_controller: 'AppController'
    ):
        
        super().__init__(loop, app_controller=app_controller)
        
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key, supress=False)
        
        self.options = self.app_config.magic_f_options
        
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
    
    async def _task(self):
        selected_option = self.gui.selected_option.get()
        
        if selected_option == "dumper":
            await self._dumper_task()
        elif selected_option == "crafter":
            await self._crafter_task()
        elif selected_option == "veggies":
            await self._veggies_task()
        else:
            await self._retrieve_task()


    async def _veggies_task(self):
        self.repetitive_task = False
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.TRANSFER_ALL,
            pre_delay=self.config.load_inventory_waiting_time,
            post_delay=self.config.transfer_all_waiting_time
        )
        
        await pa.move_cursor_and_click(
            PlayerInventoryCoordinates.TRANSFER_ALL,
            post_delay=self.config.transfer_all_waiting_time
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.CLOSE
        )
        

    async def _dumper_task(self):
        ...
        
    async def _crafter_task(self):
        ...
        
    async def _retrieve_task(self):
        ...