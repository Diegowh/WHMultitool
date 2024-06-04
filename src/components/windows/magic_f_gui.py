import tkinter as tk
from tkinter import ttk
from src.components.frames.title_frame import TitleFrame
from typing import TYPE_CHECKING

from src.components.frames.configurable_frame import ConfigurableFrame
if TYPE_CHECKING:
    from src.controllers.magic_f import MagicF

class MagicFGUI(ConfigurableFrame):
    
    def __init__(
        self,
        magic_f: 'MagicF',
        master,
        app_controller,
    ):
        super().__init__(master=master)
        
        self.master = master
        self.app_controller = app_controller
        self.service_controller = magic_f
        
        self.config = self.service_controller.config
        self.entries = {}
        self.toggle_key_label = None
        self.selected_option = None
        self.init_gui()
        
    
    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = tk.Label(self, text=f"Select mode to enable when pressing {(self.config.toggle_key).upper()}", font=("Arial", 8, "italic"), foreground="#800000")
        self.toggle_key_label.pack(pady=20)
        
        self.selection_frame = ttk.Frame(self)
        self.selection_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.selected_option = tk.StringVar()
        for name, value in self.service_controller.options.items():
            if name == "Dumper" or name == "Crafter":
                frame = ttk.Frame(self.selection_frame)
                frame.pack(anchor='w')

                radiobutton = ttk.Radiobutton(
                    frame,
                    text=name,
                    variable=self.selected_option,
                    value=value,
                )
                radiobutton.pack(side=tk.LEFT, pady=2)

                self.entries[name] = ttk.Entry(frame, width=10)
                self.entries[name].pack(side=tk.LEFT, padx=10)
            else:
                radiobutton = ttk.Radiobutton(
                    self.selection_frame,
                    text=name,
                    variable=self.selected_option,
                    value=value
                )
                radiobutton.pack(anchor='w')
            
    
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        self.app_controller.show_main()