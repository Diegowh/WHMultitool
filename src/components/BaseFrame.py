
"""
This module contains the BaseFrame class, 
which is used as a base class for all the frames in the application.

Author: DiegoWH
Date: 5/2024
"""
import tkinter as tk
from abc import ABC, abstractmethod


class BaseFrame(tk.Frame, ABC):
    """This class is used as a base class for all the frames in the application.
    It inherits from tk.Frame and is an abstract class.
    
    Has the functionallity to create the common widgets needed for all the frames.
    """
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    @abstractmethod
    def destroy_gui(self):
        """This method is used to destroy the widgets of the frame.
        """

    def destroy_screen(self):
        """This method is used to encapsulate the destruction of the frame
        and the showing of the main screen.
        
        This way when you inherit from this class,
        you don't have to worry about calling the destroy method of the frame,
        and showing the main screen.
        """
        self.destroy_gui()
        self.controller.show_main()

    def create_widgets(self):
        """This method creates the common widgets for all the frames.
        """
        back_btn = tk.Button(self, text="Back", command=self.destroy_screen)
        back_btn.pack(side=tk.BOTTOM, pady=20)
