import tkinter as tk
from config import Config
from AutoSim import AutoSim
from BreederManager import BreederManager


class AppController(tk.Tk):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        
        self.apps = {
            "AutoSim": AutoSim,
            "BreederManager": BreederManager,
        }
        
        self.title(self.config.APP_TITLE)
        self.geometry(f"{self.config.APP_WEIGHT}x{self.config.APP_HEIGHT}")
        self.resizable(False, False)

        self.main_screen = MainScreen(master=self, controller=self)
        self.main_screen.pack(fill=tk.BOTH, expand=True)

    def show_option(self, i):
        self.main_screen.pack_forget()
        app_name = list(self.apps.keys())[i]
        app_class = self.apps[app_name]
        self.current_option_screen = app_class(config=self.config, master=self, controller=self).gui
        self.current_option_screen.pack(fill=tk.BOTH, expand=True)

    def show_main(self):
        self.main_screen.pack(fill=tk.BOTH, expand=True)
        del self.current_option_screen


class MainScreen(tk.Frame):
    def __init__(self, master=None, controller: AppController=None):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        options = list(self.controller.apps.keys())
        for i, option in enumerate(options):
            btn = tk.Button(self, text=option, command=self.create_command(i))
            btn.pack(pady=10)
            
    def create_command(self, i):
        def command():
            self.controller.show_option(i)
        return command



if __name__ == "__main__":
    config = Config()
    app = AppController(config=config)
    app.mainloop()