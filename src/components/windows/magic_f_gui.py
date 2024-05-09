import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING


from src.components.frames.base_frame import BaseFrame
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.magic_f import MagicF



class MagicFGUI(BaseFrame):
    
    def __init__(self, magic_f: 'MagicF', master, app_controller, loop):
        super().__init__(master)
        self.app_controller = app_controller
        self.service_controller = magic_f
        self.config = self.service_controller.app_config
        
        self.loop = loop
        self.subservices = self.service_controller.subservices
        self.current_subservice_screen = None
        self.original_pack_configs = {}
        self.init_gui()

        
    
    def init_gui(self):
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.create_buttons()
        self.store_widget_configs()
    
    def destroy_gui(self):
        super().destroy()
        self.app_controller.show_main()
    
    
    def store_widget_configs(self):
        """
        Stores the pack configurations of all widgets.
        """
        for widget in self.winfo_children():
            self.original_pack_configs[widget] = widget.pack_info()

    def create_buttons(self):
        for key in self.subservices:
            button = ttk.Button(self, text=key, command=self.show_subservice_command(app_name=key))
            button.pack(side=tk.TOP, pady=10)
        
    def show_subservice_command(self, app_name):
        def command():
            self.service_controller.show_subservice(app_name)
        return command
    
            
