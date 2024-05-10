import asyncio
from typing import TYPE_CHECKING
from asyncio import AbstractEventLoop
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.sub.mf_keep_only_gui import MFKeepOnlyGUI
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    StructureInventoryCoordinates,
)

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
        
        self.selected_item = None
        self.selected_item_secuence = None
        
        
    def __name__(self):
        for key, value in self.app_config.magic_f_subservices.items():
           if value is MFKeepOnly:
               return key
        return None

    
    async def _drop_item(self, l: str):
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.SEARCH_BAR,
        )
        
        await pa.type_text(
            text=l,
            post_delay=0.3
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.DROP_ALL,
        )
        
    
    
    async def _task(self):
        self.selected_item = self.gui.selected_item.get()
        self.selected_item_secuence = self.app_config.keep_only_item_sequence[self.selected_item]
        print(f"Ejecutando secuencia para item: {self.selected_item}")
        print(f"Secuencia: {self.selected_item_secuence}")
        await pa.open_inventory(
            hotkey=self.config.open_dino_inventory_key,
            post_delay=0.9,
        )
        
        for l in self.selected_item_secuence:
            await self._drop_item(l)
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.CLOSE
        )