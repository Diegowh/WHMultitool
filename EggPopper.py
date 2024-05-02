import asyncio
import player_actions as pa
from screen_manager import (
    PlayerInventoryCoordinates,
)
import tkinter as tk
import keyboard
from config import Config
from BaseFrame import BaseFrame
from BaseTaskManager import BaseTaskManager

class EggPopper(BaseTaskManager):
    
    def __init__(self, loop: asyncio.AbstractEventLoop, config: Config, master, controller) -> None:
        
        super().__init__(loop=loop)
        self.config = config
        self.hotkey = self.config.EGG_POPPER_HOTKEY 
        keyboard.register_hotkey(self.hotkey, self.toggle_task, suppress=True)
        self.gui = EggPopperGUI(egg_popper=self, config=self.config, master=master, controller=controller)
        
        print("EggPopper initialized\n")
    
    async def _task(self):
        pa.open_inventory(post_delay=0.3)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR, post_delay=0.2)
        pa.type_text(text="fert", post_delay=0.2)
        pa.move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pa.pop_item()
        pa.close_inventory()
        pa.move(direction=pa.MoveDirection.LEFT, prev_delay=0.3)
        

class EggPopperGUI(BaseFrame):

    def __init__(self, egg_popper: EggPopper, config: Config, master, controller) -> None:
        super().__init__(master=master, controller=controller)
        
        self.config = config
        self.init_gui()
        self.egg_popper = egg_popper

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text="Press F1 to toggle")
        instructions_label.pack(padx=20, pady=20)

    def destroy_gui(self):
        self.egg_popper.destroy()
        super().destroy()
        print("EggPopper destroyed")