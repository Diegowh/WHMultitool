import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from src.config.settings import APP_VERSION

if TYPE_CHECKING:
    from src.controllers.app_controller import AppController

__APP_NAME__ = "All in One"

class MainScreen(tk.Frame):
    """This class represents the main screen of the app.
    """
    def __init__(self, master, controller: 'AppController'):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets of the main screen.
        """
        title_label = tk.Label(self, text=self.controller.config.app_name, font=("Arial", 15))
        title_label.pack(pady=6)

        separator_frame = tk.Canvas(self, height=1, width=250, bg='dark grey')
        separator_frame.pack(pady=(0, 10))

        self.services_container = ttk.Frame(self)
        self.services_container.pack(pady=10)
        
        options = list(self.controller.services.keys())
        
        for i, option in enumerate(options):
            btn = ttk.Button(
                self.services_container,
                text=option,
                command=self.show_option_command(i)
            )
            btn.grid(row=i, column=0, pady=10)

        footer_frame = tk.Frame(self)
        footer_frame.place(relx=0.5, rely=1, anchor='s')
        
        footer_label = tk.Label(footer_frame, text=f"{APP_VERSION} | wallhack", font=("Arial", 8, "italic"), fg="grey")
        footer_label.pack(pady=10)

    def show_option_command(self, i):
        """Method to use the show_option method with a parameter as a command.

        Args:
            i (int): Index of the selected option.
        """
        def command():
            self.controller.show_option(i)
        return command