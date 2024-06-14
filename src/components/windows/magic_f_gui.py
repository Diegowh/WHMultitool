import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.components.frames.configurable_frame import ConfigurableFrame
from src.components.frames.title_frame import TitleFrame

if TYPE_CHECKING:
    from src.controllers.service import Service


class MagicFGUI(ConfigurableFrame):
    
    def __init__(
        self,
        service_controller: 'Service',
        master,
        app_controller,
    ):
        super().__init__(master=master)

        self.selection_frame = None
        self.master = master
        self.app_controller = app_controller
        self.service_controller = service_controller
        
        self.config = self.service_controller.service_config
        self.entries = {}
        self.toggle_key_label = None
        self.selected_option = None
        self.init_gui()

    def init_gui(self):
        
        title_frame = TitleFrame(
            self,
            self.service_controller.service_title
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.toggle_key_label = tk.Label(
            self,
            text=f"Select mode to enable when pressing {self.config.toggle_key.upper()}",
            font=("Arial", 8, "italic"),
            foreground="#800000"
        )
        self.toggle_key_label.pack(pady=20)
        
        self.selection_frame = ttk.Frame(self)
        self.selection_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.selected_option = tk.StringVar(value="veggies")
        options = list(self.service_controller.options.items())
        for i in range(0, len(options), 5):  # Para que sea de columnas de maximo 5 radiobuttons por columna
            frame = ttk.Frame(self.selection_frame)
            frame.pack(side=tk.LEFT, anchor='n', padx=10)

            for name, value in options[i:i + 5]:
                if name == "Dumper" or name == "Crafter":
                    sub_frame = ttk.Frame(frame)
                    sub_frame.pack(anchor='w')

                    radiobutton = ttk.Radiobutton(
                        sub_frame,
                        text=name,
                        variable=self.selected_option,
                        value=value,
                    )
                    radiobutton.pack(side=tk.LEFT, pady=2)

                    self.entries[name] = ttk.Entry(sub_frame, width=10)
                    self.entries[name].pack(side=tk.LEFT, padx=10)
                else:
                    radiobutton = ttk.Radiobutton(
                        frame,
                        text=name,
                        variable=self.selected_option,
                        value=value
                    )
                    radiobutton.pack(anchor='w')

    def destroy_gui(self):
        self.service_controller.task_manager.destroy()
        super().destroy()
        self.app_controller.show_main()
