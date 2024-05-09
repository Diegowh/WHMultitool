import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING


from src.components.frames.base_frame import BaseFrame
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.magic_f import MagicF



class MagicFGUI(BaseFrame):
    
    def __init__(self, magic_f: 'MagicF', master, app_controller):
        super().__init__(master)
        self.app_controller = app_controller
        self.service_controller = magic_f
        self.config = self.service_controller.app_config
        
        self.services = self.service_controller.services
        self.init_gui()
    
    
    def init_gui(self):
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
    
    def destroy_gui(self):
        super().destroy()
        self.app_controller.show_main()