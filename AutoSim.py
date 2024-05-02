import asyncio
import threading
import tkinter as tk
import keyboard
import pyautogui
import time

from config import Config
from BaseFrame import BaseFrame
from BaseTaskManager import BaseTaskManager
from utils import get_screen_resolution
import player_actions as pa
from screen_manager import (
    ScreenCoordsEnum,
    ModsSelectionScreenCoordinates,
    ServerSelectionScreenCoordinates,
    GameModeScreenCoordinates,
    MainMenuScreenCoordinates,
)

class AutoSim(BaseTaskManager):
    def __init__(self, loop: asyncio.AbstractEventLoop, config: Config, master, controller) -> None:
        super().__init__(loop=loop)
        self.config = config
        self.hotkey = self.config.EGG_POPPER_HOTKEY 
        keyboard.register_hotkey(self.hotkey, self.toggle_task, suppress=True)
        self.gui = AutoSimGUI(autosim=self, config=self.config, master=master, controller=controller)

    async def _task(self):
        
        pa.move_cursor_and_click(MainMenuScreenCoordinates.PRESS_TO_START) # Press middle button on the start screen
        
        pa.move_cursor_and_click(GameModeScreenCoordinates.JOIN_GAME)  # Press Join Game button
        
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.SEARCH_BOX)  # Click on the map search bar
        pyautogui.write(self.gui.text_input.get())
        pyautogui.press('enter')
        asyncio.sleep(0.5)  # Wait for the map list to load
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.FIRST_SERVER)  # Click on the first map in the list
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.FIRST_SERVER)  # Click again to confirm the map selection, sometimes the first click doesn't register
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.JOIN)  # Click Join and wait 3 seconds for the mod selection screen to load
        pa.move_cursor_and_click(ModsSelectionScreenCoordinates.JOIN, prev_delay=3)  # Click Join
        await asyncio.sleep(10)  # Delay to allow the Server full message to appear
        pyautogui.press('esc')
        await asyncio.sleep(0.5)
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.BACK)
        pa.move_cursor_and_click(GameModeScreenCoordinates.BACK)


class AutoSimGUI(BaseFrame):

    def __init__(self, autosim: AutoSim, config: Config, master, controller) -> None:
        super().__init__(master=master, controller=controller)
        
        self.config = config
        self.autosim_label = None
        self.text_input = tk.StringVar()
        self.init_gui()
        self.autosim = autosim
        
        
        
    def init_gui(self) :
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text=f"{self.config.AUTOSIM_HOTKEY} - Toggle autosim")
        instructions_label.pack(padx=20, pady=20)
        self.autosim_label = instructions_label
        
        map_num_label = tk.Label(self, text="Map number:")
        map_num_label.pack()

        map_num_entry = tk.Entry(self, textvariable=self.text_input)
        map_num_entry.pack(padx=10, pady=10)
        
    def destroy_gui(self) -> None:
        self.autosim.destroy()
        super().destroy()
        print("AutoSim destroyed")
    