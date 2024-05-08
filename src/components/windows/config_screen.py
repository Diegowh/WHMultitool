import tkinter as tk
from src.components.frames.base_frame import BaseFrame
from src.components.frames.title_frame import TitleFrame



class ConfigScreen(BaseFrame):
    def __init__(self, service, master=None):
        super().__init__(master)
        self.service = service
        self.config = self.service.config
        self.entries = {}
        self.init_gui()

    def init_gui(self):
        title_frame = TitleFrame(
            self,
            self.config.service_name.capitalize() + " Config"
        )
        title_frame.pack(side=tk.TOP, fill=tk.X)

        config_attributes = self.config.config[self.config.service_name]
        for i, key in enumerate(config_attributes):
            value = getattr(self.config, key)
            frame = tk.Frame(self)
            frame.pack(fill=tk.X, padx=10, pady=10)
            label = tk.Label(frame, text=key, anchor='w')
            label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
            entry = tk.Entry(frame, width=5)
            entry.insert(0, str(value))
            entry.pack(side=tk.RIGHT, padx=(0, 10))
            self.entries[key] = entry

    def get_entries(self):
        return {key: entry.get() for key, entry in self.entries.items()}
    
    def save_button(self):
        save_button = tk.Button(self, text="Save", command=self.save_config)
        save_button.pack(pady=10)
        return save_button
    
    def destroy_gui(self):
        super().destroy()
        self.service.gui.pack(fill=tk.BOTH, expand=True)