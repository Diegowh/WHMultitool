"""
This module contains class which represents the GUI of the AutoEggDrop service.

AutoEggDropGUI is a subclass of BaseFrame, which is a subclass of tkinter.Frame.
"""


import tkinter as tk
from typing import TYPE_CHECKING

from src.components.windows.config_screen import ConfigScreen
from src.components.frames.configurable_frame import ConfigurableFrame

if TYPE_CHECKING:
    from src.controllers.autoeggdrop import AutoEggDrop



class AutoEggDropGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoEggDrop component.
    """
    def __init__(self, auto_eggdrop: 'AutoEggDrop', master, controller) -> None:
        super().__init__(master=master, controller=controller)

        self.master = master
        self.auto_eggdrop = auto_eggdrop
        self.config = self.auto_eggdrop.config
        self.init_gui()

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text="Press F1 to toggle")
        instructions_label.pack(padx=20, pady=20)

    def destroy_gui(self):
        self.auto_eggdrop.destroy()
        super().destroy()
        print("AutoEggDrop destroyed")

    def open_service_config(self) -> None:
        self.pack_forget()
        
        # Create the configuration screen
        config_screen = ConfigScreen(self.auto_eggdrop, self.master, self.controller).pack(fill=tk.BOTH, expand=True)
