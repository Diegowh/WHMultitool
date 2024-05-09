from typing import TYPE_CHECKING
import tkinter as tk
from src.components.frames.title_frame import TitleFrame

from src.components.frames.configurable_frame import ConfigurableFrame
if TYPE_CHECKING:
    from src.controllers.sub.mf_keep_only import MFKeepOnly
    
    
    
class MFKeepOnlyGUI(ConfigurableFrame):
    
    def __init__(self, mf_keep_only: 'MFKeepOnly', master, mf_controller):
        super().__init__(master)
        
        self.master = master
        self.mf_controller = mf_controller
        self.service_controller = mf_keep_only
        self.config = self.service_controller.config
        self.hotkey_label = None
        self.init_gui()
        
    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = tk.Label(self, text=f"Press '{(self.config.toggle_key).upper()}' to run the task", font=("Arial", 8, "italic"))
        self.toggle_key_label.pack(pady=10)
        
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        print("Magic-F -> KeepOnly, destroyed")
        self.mf_controller.show_magic_f_main()