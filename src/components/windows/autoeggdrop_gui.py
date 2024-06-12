"""
This module contains class which represents the GUI of the AutoEggDrop service.

AutoEggDropGUI is a subclass of BaseFrame, which is a subclass of tkinter.Frame.
"""


import tkinter as tk
from typing import TYPE_CHECKING


from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.autoeggdrop import AutoEggDrop


class AutoEggDropGUI(ConfigurableFrame):
    """Class that represents the GUI of the AutoEggDrop component.
    """
    def __init__(self, auto_eggdrop: 'AutoEggDrop', master, app_controller) -> None:
        super().__init__(master=master)

        self.master = master
        self.app_controller = app_controller
        self.service_controller = auto_eggdrop
        self.config = self.service_controller.service_config
        self.toggle_key_label = None
        self.init_gui()

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        title_frame = TitleFrame(
            self,
            self.service_controller.__class__.__name__
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = tk.Label(
            self,
            text=f"Press '{self.config.toggle_key.upper()}' to toggle on/off",
            font=("Arial", 8, "italic"),
            foreground="#800000"
        )
        self.toggle_key_label.pack(pady=10)

    def destroy_gui(self):
        self.service_controller.task_manager.destroy()
        super().destroy()
        self.app_controller.show_main()
