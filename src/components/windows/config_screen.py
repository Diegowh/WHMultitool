import tkinter as tk
from tkinter import messagebox

import keyboard
from src.components.frames.base_frame import BaseFrame
from src.components.frames.title_frame import TitleFrame
from tkinter import ttk
from src.utils.utils import transcript_attr_name
from src.config.service_config import ServiceConfig
from src.utils.validators import validate_time_sleep_valid_input


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

        vcmd = (self.register(validate_time_sleep_valid_input), '%P')
        config_attributes = self.config.config[self.config.service_name]
        for attr_name in config_attributes:
            value = getattr(self.config, attr_name)
            frame = tk.Frame(self)
            frame.pack(fill=tk.X, padx=10, pady=1)
            label = tk.Label(frame, text=transcript_attr_name(attr_name), anchor='w')
            label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

            entry = ttk.Entry(frame, width=5)
            entry.insert(0, str(value))
            entry.pack(side=tk.RIGHT, padx=(0, 10))
            
            if "key" in attr_name:
                button = ttk.Button(frame, text="Press Key", command=lambda entry=entry: self.press_key(entry))
                button.pack(padx=5, pady=1)
                entry.config(state='readonly')

            elif "time" in attr_name:
                entry.config(validate='key', validatecommand=vcmd)

            self.entries[attr_name] = entry

        

    def press_key(self, entry):
        entry.config(state='normal')
        entry.focus_set()
        entry.bind('<Key>', self.update_entry)

    def update_entry(self, event):
        key = event.keysym
        entry = event.widget
        entry.delete(0, 'end')
        entry.insert(0, key)
        entry.config(state='readonly')
    
    def get_entries(self):
        return {key: entry.get() for key, entry in self.entries.items()}
    
    def save_button(self, container):
        save_button = ttk.Button(container, text="Save", command=self.save_config)
        save_button.pack(side=tk.LEFT, padx=10, pady=20, expand=True)
        return save_button
    
    def save_config(self):
        entries = self.get_entries()
        self.config.update(entries)
        messagebox.showinfo(title=None, message="Config saved successfully!")
        
    def create_widgets(self):
        
        bottom_container = super().create_widgets()
        
        save_button = self.save_button(bottom_container)
        
        return bottom_container
    
    def destroy_gui(self):
        super().destroy()
        if hasattr(self.service, "register_hotkey"):
            self.service.register_hotkey(self.config.toggle_key)
            
            # Update the toggle key label
            self.service.gui.toggle_key_label.config(text=f"Press '{(self.config.toggle_key).upper()}' to toggle on/off")
    
        self.service.gui.pack(fill=tk.BOTH, expand=True)
        