import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        options = ["Option 1", "Option 2", "Option 3"]
        for i, option in enumerate(options):
            btn = tk.Button(self, text=option, command=lambda i=i: self.controller.show_option(i))
            btn.pack(pady=10)

class OptionScreen(tk.Frame):
    def __init__(self, master=None, controller=None, option=None):
        super().__init__(master)
        self.controller = controller
        self.option = option
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text=f"{self.option} chosen")
        label.pack(pady=10)

        back_btn = tk.Button(self, text="Back", command=self.controller.show_main)
        back_btn.pack(pady=10)

class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"250x200")

        self.main_screen = MainScreen(master=self, controller=self)
        self.option_screens = [OptionScreen(master=self, controller=self, option=f"Option {i+1}") for i in range(3)]

        self.show_main()

    def show_option(self, i):
        self.main_screen.pack_forget()
        self.option_screens[i].pack(fill=tk.BOTH, expand=True)

    def show_main(self):
        for screen in self.option_screens:
            screen.pack_forget()
        self.main_screen.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = AppController()
    app.mainloop()