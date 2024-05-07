"""
This module is the controller for the AutoEggDrop service.
"""


from typing import TYPE_CHECKING
import asyncio
import keyboard
import src.utils.player_actions as pa
from src.components.autoeggdrop_gui import AutoEggDropGUI
from src.controllers.base_task_manager import BaseTaskManager
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)

if TYPE_CHECKING:
    from config.config import Config
    from src.all_in_one_app import AppController

class AutoEggDrop(BaseTaskManager):
    """ 
    This class is the controller for the AutoEggDrop service.
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        controller: 'AppController',
        master
        ) -> None:

        super().__init__(loop=loop)
        self.config = config.load_service(self.__name__())
        self.toggle_key = self.config.toggle_key
        keyboard.register_hotkey(self.toggle_key, self.toggle_task, suppress=True)
        self.gui = AutoEggDropGUI(
            auto_eggdrop=self,
            config=self.config,
            master=master,
            controller=controller
            )

        print("AutoEggDrop initialized\n")

    def __name__(self):
        return "AUTOEGGDROP"

    async def _task(self):
        """Method to automate the process of dropping eggs from the inventory in the game.
        """
        pa.open_inventory(post_delay=0.3)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR, post_delay=0.2)
        pa.type_text(text="fert", post_delay=0.2)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pa.pop_item()
        pa.close_inventory()
        pa.move(direction=pa.MoveDirection.LEFT, pre_delay=0.3)
