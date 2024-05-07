"""
This module contains class which represents the GUI of the AutoEggDrop service.

AutoEggDropGUI is a subclass of BaseFrame, which is a subclass of tkinter.Frame.
"""


import tkinter as tk
from typing import TYPE_CHECKING

from src.components.base_frame import BaseFrame

if TYPE_CHECKING:
    from src.controllers.autoeggdrop import AutoEggDrop
    from config.config import Config



class AutoEggDropGUI(BaseFrame):
    """Class that represents the GUI of the AutoEggDrop component.
    """
    def __init__(self, auto_eggdrop: 'AutoEggDrop', config: 'Config', master, controller) -> None:
        super().__init__(master=master, controller=controller)

        self.config = config
        self.init_gui()
        self.auto_eggdrop = auto_eggdrop

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
