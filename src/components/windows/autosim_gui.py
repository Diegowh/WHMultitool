"""
This module contains the AutoSimGUI,
which is used as the GUI component of the Autosim class.
"""


import tkinter as tk
from typing import TYPE_CHECKING

from src.components.frames.configurable_frame import ConfigurableFrame

if TYPE_CHECKING:
    from src.controllers.autosim import AutoSim


class AutoSimGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoSim component.
    """
    def __init__(self, autosim: 'AutoSim', master, controller) -> None:
        super().__init__(master=master, controller=controller)

        self.master = master
        self.autosim_label = None
        self.text_input = tk.StringVar()
        self.autosim = autosim
        self.config = self.autosim.config
        self.init_gui()

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text=f"{self.config.toggle_key} - Toggle autosim")
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

    def open_service_config(self) -> None:
        ...
