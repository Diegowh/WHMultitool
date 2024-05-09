import asyncio
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk
from src.components.windows.magic_f_gui import MagicFGUI
if TYPE_CHECKING:
    from config.config import Config

class MagicF:
    
    def __init__(self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller,
    ):
        self.loop = loop
        self.app_config = config
        self.subservices = self.app_config.magic_f_subservices
        self.gui = MagicFGUI(
            magic_f=self,
            master=master,
            app_controller=app_controller,
            loop=loop
        )
    
    def __name__(self):
        for key, value in self.app_config.services.items():
           if value is MagicF:
               return key
        return None
    
    def show_magic_f_main(self):
        self.gui.pack(fill=tk.BOTH, expand=True)
        
        # I had to add this line to make the MainScreen visible in MacOS.
        # I didn't have this issue in Windows.
        self.update_iddle_tasks()