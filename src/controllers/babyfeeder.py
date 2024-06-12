from typing import TYPE_CHECKING
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.babyfeeder_gui import BabyFeederGUI
from src.config.config import load_service

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class BabyFeeder:
    
    def __init__(
        self,
        loop: 'AbstractEventLoop',
        config: 'Config',
        master,
        app_controller: 'AppController'
    ) -> None:

        self.service_config = load_service(self.__class__.__name__.upper())
        self.toggle_key = self.service_config.toggle_key
        self.task_manager = BaseTaskManager(
            loop=loop,
            config=config,
            app_controller=app_controller,
            service_actions=self.service_actions
        )

        self.task_manager.register_hotkey(self.toggle_key, supress=False)
        self.food_keywords = self.task_manager.app_config.food_keywords

        self.gui = BabyFeederGUI(
            babyfeeder=self,
            master=master,
            app_controller=app_controller
        )
    
    async def service_actions(self):
        
        if self.gui.mode.get() == "Loop":
            
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.SEARCH_BAR,
                pre_delay=self.service_config.load_inventory_waiting_time
            )
            
            await pa.type_text(
                text=self.food_keywords[self.gui.selected_food.get()],
                post_delay=self.service_config.after_type_text_waiting_time
            )

            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.TRANSFER_ALL,
                post_delay=self.service_config.autofeed_interval_time
            )

        elif self.gui.mode.get() == "Single":
            
            self.task_manager.repetitive_task = False
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.SEARCH_BAR,
                pre_delay=self.service_config.load_inventory_waiting_time
            )
            
            await pa.type_text(
                text=self.food_keywords[self.gui.selected_food.get()],
                post_delay=self.service_config.after_type_text_waiting_time
            )

            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.TRANSFER_ALL
            )
            await pa.move_cursor_and_click(
                PlayerInventoryCoordinates.CLOSE,
            )
            