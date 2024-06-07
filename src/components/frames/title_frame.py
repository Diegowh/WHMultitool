import tkinter as tk


class TitleFrame(tk.Frame):
    
    def __init__(self, master, title):
        super().__init__(master=master)
        self.title = title
        self.init_gui()
    
    def init_gui(self):
        """
        Initialize the GUI components.
        """
        title_label = tk.Label(self, text=self.title, font=("Arial", 15)) 
        title_label.pack(pady=6)
        
        separator_frame = tk.Canvas(self, height=1, width=250, bg='dark grey')
        separator_frame.pack(pady=(0, 10))
