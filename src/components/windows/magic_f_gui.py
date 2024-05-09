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
        self.init_gui()
    
    
    def init_gui(self):
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.create_buttons()
    
    def destroy_gui(self):
        super().destroy()
        self.app_controller.show_main()
        
    def create_buttons(self):
        for key in self.subservices:
            button = ttk.Button(self, text=key, command=self.show_option_command(app_name=key))
            button.pack(side=tk.TOP, pady=10)
            
    def show_option_command(self, app_name):
        def command():
            self.show_option(app_name)
        return command
    
            
    def show_option(self, app_name):
        for widget in self.winfo_children():
            widget.pack_forget()
        
        app_class = self.subservices[app_name]
        self.current_subservice_screen = app_class(loop=self.loop, config=self.config, master=self, mf_controller=self)
        self.current_subservice_screen.gui.pack(fill=tk.BOTH, expand=True)