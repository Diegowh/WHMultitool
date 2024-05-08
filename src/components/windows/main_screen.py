import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.app_controller import AppController


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
        options = list(self.controller.services.keys())
        for i, option in enumerate(options):
            btn = tk.Button(self, text=option, command=self.show_option_command(i))
            btn.pack(pady=10)

    def show_option_command(self, i):
        """Method to use the show_option method with a parameter as a command.

        Args:
            i (int): Index of the selected option.
        """
        def command():
            self.controller.show_option(i)
        return command
