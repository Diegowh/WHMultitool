"""
This module contains the AutoSim class,
which is used to automate the process of joining a game in the game Among Us.
"""


import asyncio
from typing import TYPE_CHECKING
import keyboard
import pyautogui
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.autosim_gui import AutoSimGUI
import src.utils.player_actions as pa
from src.utils.screen_manager import (
    ModsSelectionScreenCoordinates,
    ServerSelectionScreenCoordinates,
    GameModeScreenCoordinates,
    MainMenuScreenCoordinates,
    ConnectionFailedScreenCoordinates,
)
if TYPE_CHECKING:
    from config.config import Config
    from src.controllers.app_controller import AppController



class AutoSim(BaseTaskManager):
    """
    This class is the controller for the AutoSim service.
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller: 'AppController'
    ) -> None:

        super().__init__(loop=loop)
        self.app_config = config
        self.config = self.app_config.load_service(self.__name__().upper())
        self.toggle_key = self.config.toggle_key

        self.register_hotkey(self.toggle_key)
        self.gui = AutoSimGUI(
            autosim=self,
            master=master,

            app_controller=app_controller
        )

    def __name__(self):
        for key, value in self.app_config.services.items():
           if value is AutoSim:
               return key
        return None

    async def _task(self):
        """Method to automate the process of trying to join a full server in the game.
        """
        await pa.move_cursor_and_click(
            MainMenuScreenCoordinates.PRESS_TO_START
        ) # Press middle button on the start screen

        await pa.move_cursor_and_click(
            GameModeScreenCoordinates.JOIN_GAME
        )  # Press Join Game button

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.SEARCH_BOX
        )  # Click on the map search bar

        pyautogui.write(self.gui.text_input.get())
        pyautogui.press('enter')
        await asyncio.sleep(0.5)  # Wait for the map list to load

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.FIRST_SERVER
            )  # Click on the first map in the list

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.FIRST_SERVER
        )  # Click again to confirm the map selection, sometimes the first click doesn't register

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.JOIN,
            post_delay=self.config.mod_selection_screen_waiting_time
            )  # Click Join and wait 3 seconds for the mod selection screen to load

        await pa.move_cursor_and_click(
            ModsSelectionScreenCoordinates.JOIN,
        )  # Click Join

        await asyncio.sleep(
            self.config.server_full_screen_waiting_time
            )  # Delay to allow the Server full message to appear

        await pa.move_cursor_and_click(
            ConnectionFailedScreenCoordinates.CANCEL,
            post_delay=0.5
        )

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.BACK
        )

        await pa.move_cursor_and_click(
            GameModeScreenCoordinates.BACK
        )
