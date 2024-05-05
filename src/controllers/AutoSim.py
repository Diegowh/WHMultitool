import asyncio
import keyboard
import pyautogui

from src.config.config import Config
from src.controllers.BaseTaskManager import BaseTaskManager
import src.utils.player_actions as pa
from src.utils.screen_manager import (
    ModsSelectionScreenCoordinates,
    ServerSelectionScreenCoordinates,
    GameModeScreenCoordinates,
    MainMenuScreenCoordinates,
)

from src.components.AutoSimGUI import AutoSimGUI

class AutoSim(BaseTaskManager):
    def __init__(self, loop: asyncio.AbstractEventLoop, config: Config, master, controller) -> None:
        super().__init__(loop=loop)
        self.config = config.load_service(self.__name__())
        self.toggle_key = self.config.toggle_key

        keyboard.register_hotkey(self.toggle_key, self.toggle_task, suppress=True)
        self.gui = AutoSimGUI(autosim=self, config=self.config, master=master, controller=controller)

    def __name__(self):
        return "AUTOSIM"
    
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
        pa.move_cursor_and_click(ModsSelectionScreenCoordinates.JOIN, prev_delay=int(self.config.mod_selection_screen_waiting_time))  # Click Join
        await asyncio.sleep(int(self.config.server_full_screen_waiting_time))  # Delay to allow the Server full message to appear
        pyautogui.press('esc')
        await asyncio.sleep(0.5)
        pa.move_cursor_and_click(ServerSelectionScreenCoordinates.BACK)
        pa.move_cursor_and_click(GameModeScreenCoordinates.BACK)
