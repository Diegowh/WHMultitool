
import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from src.components.frames.title_frame import TitleFrame
from src.components.frames.configurable_frame import ConfigurableFrame

if TYPE_CHECKING:
    from src.controllers.autofarm import AutoFarm
    
    



class AutoFarmGUI(ConfigurableFrame):
    
    def __init__(
        self,
        autofarm: 'AutoFarm',
        master,
        app_controller
    ) -> None:
        super().__init__(master=master)
        
        self.master = master
        self.app_controller = app_controller
        self.service_controller = autofarm
        self.config = self.service_controller.config
        self.toggle_key_label = None
        self.init_gui()
        
    
    def init_gui(self):
        title_frame = TitleFrame(
            self,
            self.service_controller.__name__()
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = ttk.Label(
            self,
            text=f"Select to throw away when pressing {(self.config.toggle_key).upper()}",
            font=("Arial", 8, "italic"),
            foreground="#800000"
        )
        self.toggle_key_label.pack(pady=10)
        
        checkbox_container = self.checkbox_container()
        
    def destroy_gui(self):
        self.service_controller.destroy()
        super().destroy()
        self.app_controller.show_main()

    def checkbox_container(self):
        container = ttk.Frame(self)
        container.pack(padx=20, fill=tk.X)
        
        self.check_vars = {
            resource: tk.IntVar() for resource in self.service_controller.resources.keys()
        }
        
        for i, resource in enumerate(self.service_controller.resources.keys()):
            row, col = divmod(i, 4)
            checkbox = ttk.Checkbutton(
                container,
                text=resource,
                variable=self.check_vars[resource]
            )
            checkbox.grid(row=row, column=col, sticky='w')
        
        return container
    
    def get_selected_resources(self):
        return [resource for resource, var in self.check_vars.items() if var.get() == 1]