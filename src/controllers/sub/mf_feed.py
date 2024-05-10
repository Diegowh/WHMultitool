import asyncio
from typing import TYPE_CHECKING
import tkinter as tk
from src.utils import player_actions as pa
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.sub.mf_feed_gui import MFFeedGUI
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)
if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from config.config import Config
    from src.controllers.magic_f import MagicF

class MFFeed(BaseTaskManager):
    
    def __init__(
        self,
        loop: 'AbstractEventLoop',
        config: 'Config',
        master,
        mf_controller: 'MagicF'
        ) -> None:
        super().__init__(loop)
        
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        
        self.food_keywords = self.app_config.food_keywords
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key)
        
        
        print("MFFeed initialized")
        self.gui = MFFeedGUI(
            mf_feed=self,
            master=master,
            mf_controller=mf_controller
        )
        
    def __name__(self):
        for key, value in self.app_config.magic_f_subservices.items():
           if value is MFFeed:
               return key
        return None
    
    async def _task(self):
        if self.first_run:
            await pa.open_inventory(
                hotkey=self.config.open_dino_inventory_key,
                post_delay=self.config.load_inventory_waiting_time
            )
            self.first_run = False
        
        await pa.move_cursor_and_click(
            PlayerInventoryCoordinates.SEARCH_BAR,
        )
        
        await pa.type_text(
            text=self.food_keywords[self.gui.selected_food.get()],
            post_delay=self.config.after_type_text_waiting_time
        )

        await pa.move_cursor_and_click(
            PlayerInventoryCoordinates.TRANSFER_ALL,
            post_delay=self.config.autofeed_interval_time
        )
