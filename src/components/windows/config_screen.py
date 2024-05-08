import tkinter as tk
from src.components.frames.base_frame import BaseFrame


class ConfigScreen(BaseFrame):
    def __init__(self, service, master=None, controller=None):
        super().__init__(master)
        self.service = service
        self.config = self.service.config
        self.entries = {}
        self.init_gui()

    def init_gui(self):
        title_label = tk.Label(self, text=self.config.service_name)
        title_label.pack(pady=10)
        

        separator_frame = tk.Canvas(self, height=1, width=250, bg='dark grey')
        separator_frame.pack(pady=(0, 10))

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
        ...