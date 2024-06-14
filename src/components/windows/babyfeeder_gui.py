import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.components.frames.title_frame import TitleFrame
from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.windows.service_gui import ServiceGUI

if TYPE_CHECKING:
    from src.controllers.service import Service


class BabyFeederGUI(ConfigurableFrame):
    
    def __init__(
        self,
        service_controller: 'Service',
        master,
        app_controller,
    ):
        super().__init__(master=master)

        self.mode_selection_frame = None
        self.item_selection_frame = None
        self.selection_frame = None
        self.master = master
        self.app_controller = app_controller
        self.service_controller = service_controller
        
        self.config = self.service_controller.service_config
        self.foods: list[str] = self.service_controller.task_manager.app_config.foods
        self.toggle_key_label = None
        self.selected_food = None
        self.mode = None
        self.init_gui()
        
    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.service_title
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = tk.Label(
            self,
            text=f"Press '{self.config.toggle_key.upper()}' to toggle on/off",
            font=("Arial", 8, "italic"),
            foreground="#800000"
        )
        self.toggle_key_label.pack(pady=20)
        
        self.selection_frame = ttk.Frame(self)
        self.selection_frame.pack(pady=10, fill=tk.X)

        self.create_item_selection()
        self.create_mode_selection()

    def create_item_selection(self):
        self.item_selection_frame = ttk.Frame(self.selection_frame)
        self.item_selection_frame.grid(row=0, column=0, sticky='w', padx=60)

        self.selected_food = tk.StringVar(value=self.foods[0] if self.foods else None)

        for index, food in enumerate(self.foods):
            rb = ttk.Radiobutton(
                self.item_selection_frame, 
                text=food,
                variable=self.selected_food,
                value=food,
            )
            rb.grid(row=index, column=0, sticky='w')

    def create_mode_selection(self):
        self.mode = tk.StringVar(value="Single")  # Set default value to "Single"

        self.mode_selection_frame = ttk.Frame(self.selection_frame)
        self.mode_selection_frame.grid(row=0, column=1, sticky='e', padx=40)

        modes = ["Single", "Loop"]
        for index, mode in enumerate(modes):
            rb = ttk.Radiobutton(
                self.mode_selection_frame, 
                text=mode,
                variable=self.mode,
                value=mode,
            )
            rb.grid(row=index, column=0, sticky='w')

    def destroy_gui(self):
        self.service_controller.task_manager.destroy()
        super().destroy()
        self.app_controller.show_main()
