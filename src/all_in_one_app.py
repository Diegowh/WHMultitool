"""
This module is the main module of the application.
It contains the AppController class and the MainScreen class.

It is responsible for creating the main window and managing the logic of the application.

Author: Diego WH
Date 5/2024
"""

import asyncio
import tkinter as tk
from src.config.config import Config
from src.controllers.AutoSim import AutoSim
from src.controllers.AutoEggDrop import AutoEggDrop


class AppController(tk.Tk):
    """
    Main controller of the application.
    
    It is responsible for creating the main window and the main loop.
    """
    def __init__(self, config: Config, sleep_interval: float = 0.05):
        self.config = config


        # I had to add these lins to simulate Tkinter's mainloop in asyncio
        # This way I can control the mainloop for the different
        # controllers that needs to run in parallel
        self.loop = asyncio.get_event_loop()
        self.app_closing = False
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.close_app)
        self.option_add("*tearOff", 0)

        self.apps = {
            "AutoSim": AutoSim,
            "AutoEggDrop": AutoEggDrop,

        # Main Tkinter window configuration
        self.title(self.config.APP_TITLE)
        self.geometry(f"{self.config.APP_WEIGHT}x{self.config.APP_HEIGHT}")
        self.resizable(False, False)

        self.main_screen = MainScreen(master=self, controller=self)
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
            await asyncio.sleep(self.sleep_interval)


    def show_option(self, i):
        """Shows the screen of the selected option and initializes its controller.

        Args:
            i (int): Index of the selected option.
        """
        self.main_screen.pack_forget()
        app_name = list(self.apps.keys())[i]
        app_class = self.apps[app_name]
        self.current_service_screen = app_class(loop=self.loop, config=self.config, master=self, controller=self).gui
        self.current_service_screen.pack(fill=tk.BOTH, expand=True)

    def show_main(self):
        """Displays the main screen and destroys the previous service screen.
        """
        self.main_screen.pack(fill=tk.BOTH, expand=True)
        del self.current_service_screen

        # I had to add this line to make the MainScreen visible in MacOS.
        # I didn't have this issue in Windows.
        self.update_idletasks()

class MainScreen(tk.Frame):
    """This class represents the main screen of the app.
    """
    def __init__(self, master=None, controller: AppController=None):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets of the main screen.
        """
        options = list(self.controller.apps.keys())
        for i, option in enumerate(options):
            btn = tk.Button(self, text=option, command=self.show_option_command(i))
            btn.pack(pady=10)

    def show_option_command(self, i):
        """Method to use the show_option method with a parameter as a command.

        Args:
            i (int): Index of the selected option.
        """
        def command():
            self.controller.show_option(i)
        return command


async def run():
    """
    Start the main loop of the application.
    """
    config = Config()
    with AppController(config=config) as root:
        await root.mainloop()
