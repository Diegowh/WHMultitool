import asyncio
import threading
import tkinter as tk
import keyboard
import pyautogui
import time

from config import Config
from BaseFrame import BaseFrame


class AutoSimGUI(BaseFrame):

    def __init__(self, config: Config, master, controller) -> None:
        super().__init__(master=master, controller=controller)
        
        self.config = config
        
        self.autosim_label = None
        self.text_input = tk.StringVar()
        
        self.init_gui()
        
        self.autosim = AutoSim(config=self.config, gui=self)
        
    def init_gui(self) :
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text=f"{self.config.AUTOSIM_HOTKEY} - Toggle autosim")
        instructions_label.pack(padx=20, pady=20)
        self.autosim_label = instructions_label
        
        map_num_label = tk.Label(self, text="Map number:")
        map_num_label.pack()

        map_num_entry = tk.Entry(self, textvariable=self.text_input)
        map_num_entry.pack(padx=10, pady=10)
        
    def destroy(self) -> None:
        self.autosim.destroy()
        super().destroy()
        print("AutoSim destroyed")
    

class AutoSim:
    def __init__(self, config: Config, gui: AutoSimGUI):
        self.config = config
        self.autosim_task = None
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.start_loop, args=(self.loop,))
        self.thread.start()
        self.autosim_running = False  # This will track the running state internally, not in config
        keyboard.register_hotkey(self.config.AUTOSIM_HOTKEY, self.toggle_autosim, suppress=True)
        self.gui = gui


    def start_loop(self, loop: asyncio.AbstractEventLoop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
        
    def start_autosim(self):
        if not self.autosim_running:
            self.autosim_running = True
            self.loop.call_soon_threadsafe(self._start_autosim_coroutine)
            print("Auto-sim started")

    def _start_autosim_coroutine(self):
        self.autosim_task = asyncio.create_task(self.run_auto_sim())

    def stop_autosim(self):
        if self.autosim_running:
            self.autosim_running = False
            if self.autosim_task is not None:
                self.loop.call_soon_threadsafe(self._stop_autosim_coroutine)
            print("Auto-sim stopped")

    def _stop_autosim_coroutine(self):
        self.autosim_task.cancel()
    
    async def run_auto_sim(self):
        try:
            while self.autosim_running:
                map_number = self.gui.text_input.get()
                await self.autosim_routine(map_number)
            print("Auto-sim stopping")
        except Exception as e:
            print(f"Error: {e}")
            self.autosim_running = False

    def toggle_autosim(self, event=None):
        if self.autosim_running:
            self.stop_autosim()
        else:
            self.start_autosim()

    def get_screen_resolution(self):
        width, height = pyautogui.size()
        return width, height
    
    async def move_and_click(self, x, y, sleep_time=1):
        screen_w, screen_h = self.get_screen_resolution()
        # Default values are for 1920x1080 resolution, so we need to check if the resolution is different
        if screen_w != 1920 or screen_h != 1080:
            x *= screen_w / 1920
            y *= screen_h / 1080
        pyautogui.moveTo(x, y)
        pyautogui.click()
        await asyncio.sleep(sleep_time)
        
    async def autosim_routine(self, map_number):
        while self.autosim_running:
            await self.move_and_click(934, 858)  # Press middle button on the start screen
            await self.move_and_click(705, 523)  # Press Join Game button
            await self.move_and_click(1670, 200)  # Click on the map search bar
            pyautogui.write(map_number)
            pyautogui.press('enter')
            await asyncio.sleep(0.5)  # Wait for the map list to load
            await self.move_and_click(930, 335)  # Click on the first map in the list
            await self.move_and_click(930, 335)  # Click again to confirm the map selection, sometimes the first click doesn't register
            await self.move_and_click(1700, 945, 5)  # Click Join and wait 3 seconds for the mod selection screen to load
            await self.move_and_click(340, 930)  # Click Join
            await asyncio.sleep(10)  # Delay to allow the Server full message to appear
            pyautogui.press('esc')
            await asyncio.sleep(0.5)
            await self.move_and_click(170, 880)
            await self.move_and_click(964, 964)
            
    def destroy(self) -> None:
        print("Destroying AutoSim...")
        if self.autosim_task is not None:
            self.loop.call_soon_threadsafe(self.loop.stop)
        # TODO: El while se llama infinitamente si no se ha iniciado el autosim
        while self.loop.is_running():
            time.sleep(0.1)
        self.loop.close()
        self.thread.join()
