import asyncio
import tkinter as tk
from config import Config
from AutoSim import AutoSim
from EggPopper import EggPopper


class AppController(tk.Tk):
    def __init__(self, config: Config, sleep_interval: float = 0.05):
        self.config = config
        
        self.sleep_interval = sleep_interval
        self.app_closing = False
        self.loop = asyncio.get_event_loop()
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.close_app)
        self.option_add("*tearOff", 0)
        
        self.apps = {
            "AutoSim": AutoSim,
            "EggPopper": EggPopper,
        }
        
        self.title(self.config.APP_TITLE)
        self.geometry(f"{self.config.APP_WEIGHT}x{self.config.APP_HEIGHT}")
        self.resizable(False, False)

        self.main_screen = MainScreen(master=self, controller=self)
        self.main_screen.pack(fill=tk.BOTH, expand=True)

    
    def __enter__(self):
        return self
    
    def __exit__(self, *_x):
        self.destroy()
        
    def close_app(self):
        self.app_closing = True
    
    async def mainloop(self, _n=0):
        while not self.app_closing:
            self.update()
            await asyncio.sleep(self.sleep_interval)
    
    
    def show_option(self, i):
        self.main_screen.pack_forget()
        app_name = list(self.apps.keys())[i]
        app_class = self.apps[app_name]
        self.current_option_screen = app_class(loop=self.loop, config=self.config, master=self, controller=self).gui
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


async def main():
    config = Config()
    with AppController(config=config) as root:
        await root.mainloop()


if __name__ == "__main__":
    asyncio.run(main())