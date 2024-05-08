import tkinter as tk
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.base_task_manager import BaseTaskManager



class BaseConfigFrame(tk.Frame):
    def __init__(self, service: 'BaseTaskManager', master=None, controller=None):
        super().__init__(master)
        self.service = service
        self.config = self.service.config
        self.entries = {}
        self.init_gui()

    def init_gui(self):
        config_attributes = self.config.config[self.config.service_name]
        for i, key in enumerate(config_attributes):
            value = getattr(self.config, key)
            label = tk.Label(self, text=key)
            label.grid(row=i, column=0, padx=10, pady=10)
            entry = tk.Entry(self)
            entry.insert(0, str(value))
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[key] = entry

    def get_entries(self):
        return {key: entry.get() for key, entry in self.entries.items()}