import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

import keyboard

from src.components.frames.base_frame import BaseFrame
from src.components.windows.config_screen import ConfigScreen
if TYPE_CHECKING:
    from src.controllers.task_manager import TaskManager


class ConfigurableFrame(BaseFrame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def open_service_config(self, service: 'TaskManager') -> None:
        keyboard.unregister_all_hotkeys()
        self.pack_forget()
        
        # Create the configuration screen
        config_screen = (ConfigScreen(service, self.master))
        config_screen.pack(fill=tk.BOTH, expand=True)
 
    def config_btn(self, container) -> ttk.Button:
        config_button = ttk.Button(container, text="Config", command=lambda: self.open_service_config(self.service_controller))
        config_button.pack(side=tk.LEFT, padx=10, pady=20, expand=True)
        return config_button

    def create_widgets(self):
        """This method creates the common widgets for all the frames.
        """
        
        bottom_container = super().create_widgets()
        
        config_button = self.config_btn(bottom_container)
        
        return bottom_container
