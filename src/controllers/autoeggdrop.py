"""
This module is the controller for the AutoEggDrop service.
"""


import asyncio
from typing import TYPE_CHECKING

from src.components.windows.autoeggdrop_gui import AutoEggDropGUI
from src.controllers.service import Service
from src.utils import player_actions as pa
from src.utils.screen_manager import PlayerInventoryCoordinates

if TYPE_CHECKING:
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class AutoEggDrop(Service):
    """ 
    This class is the controller for the AutoEggDrop service.
    """
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
            gui=AutoEggDropGUI,
        )
        super().init_gui()
    async def on_toggle_key(self):
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
