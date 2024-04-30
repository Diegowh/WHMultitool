import tkinter as tk
from abc import ABC, abstractmethod


class BaseFrame(tk.Frame, ABC):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    @abstractmethod
    def destroy_screen(self):
        pass
    
    def create_widgets(self):
        back_btn = tk.Button(self, text="Back", command=self.destroy_screen)
        back_btn.pack(side=tk.BOTTOM, pady=20)