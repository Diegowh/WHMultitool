"""
This module contains the BaseFrame class, 
which is used as a base class for all the frames in the application.
"""


import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class BaseFrame(tk.Frame, ABC):
    """This class is used as a base class for all the frames in the application.
    It inherits from tk.Frame and is an abstract class.
    
    Has the functionallity to create the common widgets needed for all the frames.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    @abstractmethod
    def destroy_gui(self):
        """This method is used to destroy the widgets of the frame.
        """

    # def destroy_screen(self):
    #     """This method is used to encapsulate the destruction of the frame
    #     and the showing of the main screen.
        
    #     This way when you inherit from this class,
    #     you don't have to worry about calling the destroy method of the frame,
    #     and showing the main screen.
    #     """
    #     self.destroy_gui()

    def back_btn(self, container):
        back_btn = ttk.Button(container, text="Back", command=self.destroy_gui)
        back_btn.pack(side=tk.LEFT, padx=10, pady=20, expand=True)
        return back_btn

    def bottom_container(self) -> tk.Frame:
        bottom_container = tk.Frame(self)
        bottom_container.pack(side=tk.BOTTOM, fill=tk.X)
        return bottom_container

    def create_widgets(self) -> tk.Frame:
        """This method creates the common widgets for all the frames.
        """
        bottom_container = self.bottom_container()
        back_btn = self.back_btn(bottom_container)

        return bottom_container