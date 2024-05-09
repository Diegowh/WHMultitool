from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk
from src.components.frames.title_frame import TitleFrame

from src.components.frames.configurable_frame import ConfigurableFrame

if TYPE_CHECKING:
    from src.controllers.sub.mf_feed import MFFeed
    

class MFFeedGUI(ConfigurableFrame):
    
    def __init__(self, mf_feed: 'MFFeed', master, mf_controller):
        super().__init__(master)
        
        self.master = master
        self.mf_controller = mf_controller
        self.service_controller = mf_feed
        self.config = self.service_controller.config
        self.init_gui()
        print("GUI -> Feed, initialized")

    def init_gui(self):
        
        label = ttk.Label(
            self,
            text="Feed"
        )
        label.pack(side=tk.TOP, pady=10)
        # title_frame = TitleFrame(
        #     self,
        #     self.service_controller.__name__()
        # )
        # title_frame.pack(side=tk.TOP, fill=tk.X)

    
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        print("Magic-F -> Feed, destroyed")
        self.mf_controller.show_magic_f_main()