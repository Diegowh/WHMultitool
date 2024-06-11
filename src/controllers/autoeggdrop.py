"""
This module is the controller for the AutoEggDrop service.
"""


from typing import TYPE_CHECKING
import asyncio
import src.utils.player_actions as pa
from src.components.windows.autoeggdrop_gui import AutoEggDropGUI
from src.controllers.base_task_manager import BaseTaskManager
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)
from src.config.config import load_service

if TYPE_CHECKING:
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class AutoEggDrop(BaseTaskManager):
    """ 
    This class is the controller for the AutoEggDrop service.
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',

        app_controller: 'AppController',
        master
    ) -> None:

        super().__init__(loop=loop, app_controller=app_controller)

        self.app_config = config
        self.service_config = load_service(self.__class__.__name__.upper())
        self.toggle_key = self.service_config.toggle_key
        self.register_hotkey(self.toggle_key)
        self.gui = AutoEggDropGUI(
            auto_eggdrop=self,
            master=master,
            app_controller=app_controller
            )

    async def _task(self):
        """Method to automate the process of dropping eggs from the inventory in the game.
        """
        await pa.open_inventory(
            hotkey=self.service_config.inventory_key,
            post_delay=self.service_config.load_inventory_waiting_time
        )
        await pa.move_cursor_and_click(
            location=PlayerInventoryCoordinates.SEARCH_BAR,
            post_delay=0.2
        )
        
        await pa.type_text(text="fert", post_delay=0.2)
        await pa.move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT)
        await pa.pop_item(
            hotkey=self.service_config.pop_item_key,
            post_delay=self.service_config.after_pop_waiting_time
        )
        await pa.close_inventory()
        await pa.move(
            direction=self.service_config.move_direction_key,
            duration =self.service_config.move_duration_time,
            pre_delay=0.3
        )
