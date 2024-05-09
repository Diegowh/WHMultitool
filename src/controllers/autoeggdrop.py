"""
This module is the controller for the AutoEggDrop service.
"""


from typing import TYPE_CHECKING
import asyncio
import keyboard
import src.utils.player_actions as pa
from src.components.windows.autoeggdrop_gui import AutoEggDropGUI
from src.controllers.base_task_manager import BaseTaskManager
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)

if TYPE_CHECKING:
    from config.config import Config
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

        super().__init__(loop=loop)
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        self.toggle_key = self.config.toggle_key
        self.register_hotkey(self.toggle_key)
        self.gui = AutoEggDropGUI(
            auto_eggdrop=self,
            master=master,
            app_controller=app_controller
            )

        print("AutoEggDrop initialized\n")



    async def _task(self):
        """Method to automate the process of dropping eggs from the inventory in the game.
        """
        await pa.open_inventory(
            hotkey=self.config.pop_item_key,
            post_delay=0.3
        )
        await pa.move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR, post_delay=0.2)
        await pa.type_text(text="fert", post_delay=0.2)
        await pa.move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        await pa.pop_item(
            hotkey=self.config.pop_item_key,
        )
        await pa.close_inventory()
        await pa.move(
            direction=self.config.move_direction_key,
            pre_delay=0.3
        )
