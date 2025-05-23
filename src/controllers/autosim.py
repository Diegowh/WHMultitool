"""
This module contains the AutoSim class,
which is used to automate the process of joining a game in the game Among Us.
"""


import asyncio
from typing import TYPE_CHECKING
import pyautogui

from src.components.windows.autosim_gui import AutoSimGUI
from src.controllers.service import Service
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    ModsSelectionScreenCoordinates,
    ServerSelectionScreenCoordinates,
    GameModeScreenCoordinates,
    MainMenuScreenCoordinates,
    ConnectionFailedScreenCoordinates,
)

if TYPE_CHECKING:
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class AutoSim(Service):
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
        super().__init__(
            loop=loop,
            config=config,
            master=master,
            app_controller=app_controller,
            gui=AutoSimGUI,
        )

        super().init_gui()
    async def on_toggle_key(self):
        """Method to automate the process of trying to join a full server in the game.
        """
        await pa.move_cursor_and_click(
            MainMenuScreenCoordinates.PRESS_TO_START
        )  # Press middle button on the start screen

        await pa.move_cursor_and_click(
            GameModeScreenCoordinates.JOIN_GAME
        )  # Press Join Game button

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.SEARCH_BOX
        )  # Click on the map search bar

        pyautogui.write(self.gui.text_input.get())
        pyautogui.press('enter')
        await asyncio.sleep(self.service_config.map_list_loading_waiting_time)  # Wait for the map list to load

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.FIRST_SERVER
            )  # Click on the first map in the list

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.FIRST_SERVER
        )  # Click again to confirm the map selection, sometimes the first click doesn't register

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.JOIN,
            post_delay=self.service_config.mod_selection_screen_waiting_time
            )  # Click Join and wait 3 seconds for the mod selection screen to load

        await pa.move_cursor_and_click(
            ModsSelectionScreenCoordinates.JOIN,
            post_delay=self.service_config.server_full_screen_waiting_time
        )  # Click Join

        await pa.move_cursor_and_click(
            ConnectionFailedScreenCoordinates.CANCEL,
            post_delay=self.service_config.back_to_main_menu_waiting_time
        )

        await pa.move_cursor_and_click(
            ServerSelectionScreenCoordinates.BACK,
            post_delay=self.service_config.back_to_main_menu_waiting_time
        )

        await pa.move_cursor_and_click(
            GameModeScreenCoordinates.BACK,
            post_delay=self.service_config.back_to_main_menu_waiting_time
        )
