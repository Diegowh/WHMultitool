from tkinter import ttk
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
        
        self.items: list[str] = self.mf_controller.app_config.keep_only_items
        self.selected_item = None
        self.hotkey_label = None
        self.init_gui()
        
    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.item_selection_frame = ttk.Frame(self)
        self.item_selection_frame.pack(pady=10)
        
        self.create_item_selection()
        
        self.toggle_key_label = tk.Label(self, text=f"Press '{(self.config.toggle_key).upper()}' to run the task", font=("Arial", 8, "italic"))
        self.toggle_key_label.pack(pady=10)
        
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        print("Magic-F -> KeepOnly, destroyed")
        self.mf_controller.show_magic_f_main()
        
    def create_item_selection(self):
        self.selected_item = tk.StringVar(value=self.items[0] if self.items else None)
        
        for index,item in enumerate(self.items):
            rb = ttk.Radiobutton(
                self.item_selection_frame,
                text=item,
                variable=self.selected_item,
                value=item,
            )
            rb.grid(row=index, column=0, sticky='w')