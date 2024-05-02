from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controllers.AutoSim import AutoSim
    from src.config.config import Config
    

from src.components.BaseFrame import BaseFrame
import tkinter as tk

class AutoSimGUI(BaseFrame):

    def __init__(self, autosim: 'AutoSim', config: 'Config', master, controller) -> None:
        super().__init__(master=master, controller=controller)
        
        self.config = config
        self.autosim_label = None
        self.text_input = tk.StringVar()
        self.init_gui()
        self.autosim = autosim
        
        
        
    def init_gui(self):
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
    