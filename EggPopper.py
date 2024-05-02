import asyncio
from player_actions import *
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
        
        self.config = config
        self.hotkey = self.config.EGG_POPPER_HOTKEY
        super().__init__(loop=loop)
        self.gui = EggPopperGUI(egg_popper=self, config=self.config, master=master, controller=controller)
        
        print("EggPopper initialized\n")
    
    async def _task(self):
        open_inventory(post_delay=0.3)
        move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR, post_delay=0.2)
        type_text(text="fert", post_delay=0.2)
        move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pop_item()
        close_inventory()
        move(direction=MoveDirection.LEFT, prev_delay=0.3)
        await asyncio.sleep(0)

    def register_key(self):
        keyboard.register_hotkey(self.hotkey, self.toggle_task, suppress=True)
        print(f"Registered hotkey: {self.hotkey}")
        
    def unregister_key(self):
        keyboard.unregister_hotkey(self.hotkey)
        print(f"Unregistered hotkey: {self.hotkey}")

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