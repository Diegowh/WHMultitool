"""
This module is the main module of the application.
It contains the AppController class and the MainScreen class.

It is responsible for creating the main window and managing the logic of the application.

Author: Diego WH
Date 5/2024
"""

import asyncio
import base64
import tempfile
import tkinter as tk
from tkinter import messagebox

import pygetwindow as gw

from src.components.windows.main_screen import MainScreen
from src.config.config import Config, ARK_ASCENDED_WINDOW_TITLE
from src.controllers.autosim import AutoSim
from src.controllers.autoeggdrop import AutoEggDrop
from src.controllers.babyfeeder import BabyFeeder
from src.controllers.autofarm import AutoFarm
from src.controllers.magic_f import MagicF


class AppController(tk.Tk):
    """
    Main controller of the application.
    
    It is responsible for creating the main window and the main loop.
    """
    def __init__(self, config: Config):
        self.config = config

        # I had to add these lines to simulate Tkinter's mainloop in asyncio
        # This way I can control the mainloop for the different
        # controllers that needs to run in parallel
        self.loop = asyncio.get_event_loop()
        self.app_closing = False
        super().__init__()
        self.protocol(self.config.delete_window_protocol, self.close_app)
        self.option_add(self.config.option_pattern, 0)
        self.is_ark_in_focus = False
        self.services = {
            AutoSim: "Auto-Sim",
            AutoEggDrop: "Auto-Eggdrop",
            BabyFeeder: "Baby Feeder",
            AutoFarm: "Auto-Farm",
            MagicF: "Magic-F"
        }

        try:
            with open("src/assets/asset.txt", "r") as f:
                encoded_str = f.read()
        except FileNotFoundError:
            self.withdraw()
            messagebox.showerror("Error", "Asset file not found. Make sure the src folder is in the same directory as the executable.")
            self.destroy()
            return

        image_data = base64.b64decode(encoded_str)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ico") as temp_icon:
            temp_icon.write(image_data)
            self.iconbitmap(temp_icon.name)

        # Main Tkinter window configuration
        self.title(self.config.app_title)
        self.geometry(f"{self.config.app_width}x{self.config.app_height}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.main_screen = MainScreen(master=self, app_controller=self)
        self.main_screen.pack(fill=tk.BOTH, expand=True)
        self.current_service_screen = None

    def __enter__(self):
        return self

    def __exit__(self, *_x):
        self.destroy()

    def close_app(self) -> None:
        """Flag to close the app.
        """
        self.app_closing = True

    async def mainloop(self, _n=0): # pylint: disable=W0236
        while not self.app_closing:
            self.update()
            self.is_ark_in_focus = self.check_if_ark_in_focus()
            await asyncio.sleep(self.config.main_loop_sleep_interval)

    def show_option(self, class_):
        """Shows the screen of the selected option and initializes its controller.

        Args:
            class_ (callable): Class controller of the selected option.
        """
        self.main_screen.pack_forget()

        self.current_service_screen = class_(
            loop=self.loop,
            config=self.config,
            master=self,
            app_controller=self
        ).gui
        self.current_service_screen.pack(fill=tk.BOTH, expand=True)

    def show_main(self):
        """Displays the main screen and destroys the previous service screen.
        """
        self.main_screen.pack(fill=tk.BOTH, expand=True)
        del self.current_service_screen # I think this is not necessary but I did it to be sure

        # I had to add this line to make the MainScreen visible in MacOS.
        # I didn't have this issue in Windows.
        self.update_idletasks()

    @staticmethod
    def check_if_ark_in_focus() -> bool:
        try:
            active_window_title = gw.getActiveWindowTitle()
        except Exception:
            return False

        return active_window_title == ARK_ASCENDED_WINDOW_TITLE


async def run():
    """
    Start the main loop of the application.
    """
    config = Config()
    with AppController(config=config) as root:
        await root.mainloop()
