"""
This module contains the AutoSimGUI,
which is used as the GUI component of the Autosim class.
"""


import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.windows.service_gui import ServiceGUI
from src.components.frames.title_frame import TitleFrame
from src.utils.validators import validate_map_number

if TYPE_CHECKING:
    from src.controllers.service import Service


class AutoSimGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoSim component.
    """
    def __init__(
            self,
            service_controller: 'Service',
            master,
            app_controller
    ) -> None:
        super().__init__(master=master)

        self.master = master
        self.app_controller = app_controller
        self.text_input = tk.StringVar()
        self.service_controller = service_controller
        self.config = self.service_controller.service_config
        self.toggle_key_label = None
        self.init_gui()

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        
        title_frame = TitleFrame(
            self,
            self.service_controller.service_title
        )
        
        title_frame.pack(side=tk.TOP, fill=tk.X)

        self.toggle_key_label = ttk.Label(self, text=f"Press '{self.config.toggle_key.upper()}' to toggle on/off", font=("Arial", 8, "italic"), foreground="#800000")
        self.toggle_key_label.pack(pady=10)
        
        map_num_frame = tk.Frame(self)
        map_num_frame.pack(padx=10, pady=10)
        
        map_num_label = tk.Label(map_num_frame, text="Map number:", anchor='w')
        map_num_label.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10)
        
        vcmd = (self.register(validate_map_number), '%P')
        map_num_entry = ttk.Entry(map_num_frame, textvariable=self.text_input, width=5, validate='key', validatecommand=vcmd)
        map_num_entry.pack(side=tk.RIGHT, padx=(10, 10))
    
    def destroy_gui(self) -> None:
        self.service_controller.task_manager.destroy()
        super().destroy()
        self.app_controller.show_main()
