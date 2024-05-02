from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.AutoEggDrop import AutoEggDrop
    from config.config import Config

from src.components.BaseFrame import BaseFrame
import tkinter as tk


class AutoEggDropGUI(BaseFrame):

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