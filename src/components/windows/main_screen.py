import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.config.config import APP_VERSION

if TYPE_CHECKING:
    from src.controllers.app_controller import AppController

__APP_NAME__ = "All in One"


class MainScreen(ctk.CTkFrame):
    """This class represents the main screen of the app.
    """
    def __init__(self, master, app_controller: 'AppController'):
        super().__init__(master)
        self.services_container = None
        self.app_controller = app_controller
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets of the main screen.
        """
        title_label = ctk.CTkLabel(self, text=self.app_controller.config.app_name, font=("Arial", 15))
        title_label.pack(pady=6)

        separator_frame = ctk.CTkCanvas(self, height=1, width=250, bg='dark grey')
        separator_frame.pack(pady=(0, 10))

        self.services_container = ctk.CTkFrame(self)
        self.services_container.pack(pady=10)
        
        for i, (class_, title_name) in enumerate(self.app_controller.services.items()):
            btn = ctk.CTkButton(
                self.services_container,
                text=title_name,
                command=self.show_option_command(class_)
            )
            btn.grid(row=i, column=0, pady=10)

        footer_frame = ctk.CTkFrame(self)
        footer_frame.place(relx=0.5, rely=1, anchor='s')
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text=f"{APP_VERSION} | wallhack",
            font=("Arial", 8, "italic"),
            text_color="grey"
        )
        footer_label.pack(pady=10)

    def show_option_command(self, class_):
        """Method to use the show_option method with a parameter as a command.

        Args:
            class_ (str): Class controller of the selected option.
        """
        def command():
            self.app_controller.show_option(class_)
        return command
