import tkinter as tk
from abc import ABC, abstractmethod

from src.components.base_frame import BaseFrame


class ConfigurableFrame(BaseFrame):
    
    def __init__(self, master=None, controller=None):
        super().__init__(master, controller)
    
    @abstractmethod
    def open_service_config(self):
        """This method is used to open the configuration window of the service."""
        
    def config_btn(self, container):
        config_button = tk.Button(container, text="Config", command=self.open_service_config)
        config_button.pack(side=tk.LEFT, padx=10, pady=20, expand=True)
        return config_button

    def create_widgets(self):
        """This method creates the common widgets for all the frames.
        """
        
        bottom_container = super().create_widgets()
        
        config_button = self.config_btn(bottom_container)
        
        return bottom_container
