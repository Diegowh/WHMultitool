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
        
        self.foods: list[str] = self.mf_controller.app_config.foods
        print(self.foods)
        self.toggle_key_label = None
        self.selected_food = None
        self.init_gui()

    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        

        self.create_food_selection()
        
        self.toggle_key_label = tk.Label(self, text=f"Press '{(self.config.toggle_key).upper()}' to toggle on/off", font=("Arial", 8, "italic"))
        self.toggle_key_label.pack(pady=20)

    def create_food_selection(self):
        self.selected_food = tk.StringVar(value=self.foods[0] if self.foods else None)
        
        for food in self.foods:
            rb = ttk.Radiobutton(
                self,
                text=food,
                variable=self.selected_food,
                value=food,
            )
            rb.pack()
            
    
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        print("Magic-F -> Feed, destroyed")
        self.mf_controller.show_magic_f_main()