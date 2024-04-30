import asyncio
from player_actions import *
from screen_manager import (
    PlayerInventoryCoordinates,
)
import tkinter as tk
from threading import Thread
import keyboard
from config import Config
from BaseFrame import BaseFrame
from BaseTaskManager import BaseTaskManager

class EggPopper(BaseTaskManager):
    
    def __init__(self, config: Config, master, controller) -> None:
        super().__init__()
        self.config = config
        self.gui = EggPopperGUI(egg_popper=self, config=self.config, master=master, controller=controller)
        
        keyboard.register_hotkey('f1', self.toggle_task, suppress=True)
        print("EggPopper initialized\n")
    
    def _task_routine(self):
        open_inventory()
        move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR)
        type_text(text="fertilized egg", post_delay=0.2)
        move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pop_item()
        close_inventory()
        move(direction=MoveDirection.LEFT, prev_delay=0.3)



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
        self.egg_popper.destroy_loop()
        super().destroy()
        print("EggPopper destroyed")