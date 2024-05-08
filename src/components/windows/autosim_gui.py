"""
This module contains the AutoSimGUI,
which is used as the GUI component of the Autosim class.
"""


import tkinter as tk
from typing import TYPE_CHECKING

from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.windows.config_screen import ConfigScreen
from src.utils.validators import validate_map_number
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.autosim import AutoSim


class AutoSimGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoSim component.
    """
    def __init__(self, autosim: 'AutoSim', master, controller) -> None:
        super().__init__(master=master)

        self.master = master
        self.controller = controller
        self.text_input = tk.StringVar()
        self.autosim = autosim
        self.config = self.autosim.config
        self.init_gui()

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        
        title_frame = TitleFrame(
            self,
            self.config.service_name.capitalize()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        map_num_frame = tk.Frame(self)
        map_num_frame.pack(padx=10, pady=10)
        
        map_num_label = tk.Label(map_num_frame, text="Map number:", anchor='w')
        map_num_label.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10)
        
        vcmd = (self.register(validate_map_number), '%P')
        map_num_entry = tk.Entry(map_num_frame, textvariable=self.text_input, width=5, validate='key', validatecommand=vcmd)
        map_num_entry.pack(side=tk.RIGHT, padx=(10, 10))
    
        toggle_key_label = tk.Label(self, text=f"Press '{(self.config.toggle_key).upper()}' to toggle on/off", font=("Arial", 8, "italic"))
        toggle_key_label.pack(pady=10)
    
    def destroy_gui(self) -> None:
        self.autosim.destroy()
        super().destroy()
        print("AutoSim destroyed")
        self.controller.show_main()

    def open_service_config(self) -> None:
        
        # Hide the current frame
        self.pack_forget()
        
        # Create the configuration screen
        config_screen = ConfigScreen(self.autosim, self.master).pack(fill=tk.BOTH, expand=True)
