import asyncio
from src.components.AutoEggDropGUI import AutoEggDropGUI
import src.utils.player_actions as pa
from src.utils.screen_manager import (
    PlayerInventoryCoordinates,
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from config.config import Config
    
import keyboard
from src.controllers.BaseTaskManager import BaseTaskManager

class AutoEggDrop(BaseTaskManager):
    
    def __init__(self, loop: asyncio.AbstractEventLoop, config: 'Config', master, controller) -> None:
        
        super().__init__(loop=loop)
        self.config = config.load_service(self.__name__())
        self.toggle_key = self.config.toggle_key 
        keyboard.register_hotkey(self.toggle_key, self.toggle_task, suppress=True)
        self.gui = AutoEggDropGUI(auto_eggdrop=self, config=self.config, master=master, controller=controller)
        
        print("AutoEggDrop initialized\n")
    
    def __name__(self):
        return "AUTOEGGDROP"
    
    async def _task(self):
        pa.open_inventory(post_delay=0.3)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR, post_delay=0.2)
        pa.type_text(text="fert", post_delay=0.2)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pa.pop_item()
        pa.close_inventory()
        pa.move(direction=pa.MoveDirection.LEFT, prev_delay=0.3)
