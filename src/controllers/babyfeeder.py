import asyncio
from typing import TYPE_CHECKING

from src.components.windows.babyfeeder_gui import BabyFeederGUI
from src.controllers.service import Service
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class BabyFeeder(Service):

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller: 'AppController'
    ) -> None:
        super().__init__(
            loop=loop,
            config=config,
            master=master,
            app_controller=app_controller,
            gui=BabyFeederGUI,
            supress_hotkey=False
        )
        self.food_keywords = self.task_manager.app_config.food_keywords
        super().init_gui()

    async def on_toggle_key(self):
        
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
            