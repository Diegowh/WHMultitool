from typing import TYPE_CHECKING
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.babyfeeder_gui import BabyFeederGUI

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from config.config import Config
    from src.controllers.app_controller import AppController

class BabyFeeder(BaseTaskManager):
    
    def __init__(
        self,
        loop: 'AbstractEventLoop',
        config: 'Config',
        master,
        app_controller: 'AppController'
    ) -> None:
        
        super().__init__(loop)
        
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        
        self.food_keywords = self.app_config.food_keywords
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key, supress=False)
        
        self.gui = BabyFeederGUI(
            babyfeeder=self,
            master=master,
            app_controller=app_controller
        )
    
    def __name__(self):
        for key, value in self.app_config.services.items():
           if value is BabyFeeder:
               return key
        return None
    
    async def _task(self):
        print(f"BabyFeeder mode: {self.gui.mode.get()}")
        
        if self.gui.mode.get() == "Loop":
            
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.SEARCH_BAR,
                pre_delay=self.config.load_inventory_waiting_time
            )
            
            await pa.type_text(
                text=self.food_keywords[self.gui.selected_food.get()],
                post_delay=self.config.after_type_text_waiting_time
            )

            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.TRANSFER_ALL,
                post_delay=self.config.autofeed_interval_time
            )

        elif self.gui.mode.get() == "Single":
            
            self.repetitive_task = False
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.SEARCH_BAR,
                pre_delay=self.config.load_inventory_waiting_time
            )
            
            await pa.type_text(
                text=self.food_keywords[self.gui.selected_food.get()],
                post_delay=self.config.after_type_text_waiting_time
            )

            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.TRANSFER_ALL
            )
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.CLOSE,
            )
            