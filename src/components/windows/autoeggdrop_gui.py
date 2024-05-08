"""
This module contains class which represents the GUI of the AutoEggDrop service.

AutoEggDropGUI is a subclass of BaseFrame, which is a subclass of tkinter.Frame.
"""


import tkinter as tk
from typing import TYPE_CHECKING

from src.components.windows.config_screen import ConfigScreen
from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.autoeggdrop import AutoEggDrop



class AutoEggDropGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoEggDrop component.
    """
    def __init__(self, auto_eggdrop: 'AutoEggDrop', master, controller) -> None:
        super().__init__(master=master)

        self.master = master
        self.controller = controller
        self.auto_eggdrop = auto_eggdrop
        self.config = self.auto_eggdrop.config
        self.toggle_key_label = None
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
        
        self.toggle_key_label = tk.Label(self, text=f"Press '{(self.config.toggle_key).upper()}' to toggle on/off", font=("Arial", 8, "italic"))
        self.toggle_key_label.pack(pady=10)

    def destroy_gui(self):
        self.auto_eggdrop.destroy()
        super().destroy()
        print("AutoEggDrop destroyed")
        self.controller.show_main()
        

    def open_service_config(self) -> None:
        self.pack_forget()
        
        # Create the configuration screen
        config_screen = ConfigScreen(self.auto_eggdrop, self.master).pack(fill=tk.BOTH, expand=True)
