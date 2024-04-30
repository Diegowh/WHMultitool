import asyncio
from player_actions import *
from screen_manager import (
    PlayerInventoryCoordinates,
)
import tkinter as tk
from threading import Thread
import keyboard
from config import Config
from BaseFrame import BaseFrame
import utils




class BreederManager:
    
    def __init__(self, config: Config, master, controller) -> None:
        self.config = config
        self.gui = BreederManagerGUI(breeder_manager=self, config=self.config, master=master, controller=controller)
        self.autoeggdrop_task = None
        self.loop = asyncio.new_event_loop()
        self.thread = Thread(target=self.start_loop, args=(self.loop,))
        self.thread.start()
        self.autoeggdrop_running = False
        keyboard.register_hotkey('f1', self.toggle_autoeggdrop, suppress=True)
        print("BreederManager initialized\n")
        
    def start_loop(self, loop: asyncio.AbstractEventLoop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def start_autoeggdrop(self):
        assert not self.autoeggdrop_running
        self.autoeggdrop_running = True
        self.loop.call_soon_threadsafe(self._start_autoeggdrop_coroutine)
        print("Auto-eggdrop started\n")

    def _start_autoeggdrop_coroutine(self):
        self.autoeggdrop_task = asyncio.create_task(self.run_autoeggdrop())

    def stop_autoeggdrop(self):
        if self.autoeggdrop_running:
            self.autoeggdrop_running = False
            if self.autoeggdrop_task is not None:
                self.loop.call_soon_threadsafe(self._stop_autoeggdrop_coroutine)

    def _stop_autoeggdrop_coroutine(self):
        self.autoeggdrop_task.cancel()

    async def run_autoeggdrop(self):
        try:
            while self.autoeggdrop_running:
                self._autoeggdrop_routine()
        except Exception as e:
            print(f"Error: {e}")
            self.autoeggdrop_running = False

    def toggle_autoeggdrop(self, event=None):
        if self.autoeggdrop_running:
            self.stop_autoeggdrop()
        elif self.autoeggdrop_task is None or self.autoeggdrop_task.done():
            self.start_autoeggdrop()
    
    def _autoeggdrop_routine(self):
        open_inventory()
        move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR)
        type_text(text="fertilized egg", post_delay=0.2)
        move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
        pop_item()
        close_inventory()
        move(direction=MoveDirection.LEFT, prev_delay=0.3)


    def destroy_loop(self):
        print("Destroying BreederManager...")
        self.loop.call_soon_threadsafe(self.loop.stop)
        while self.loop.is_running():
            time.sleep(0.1)
        self.loop.close()
        self.thread.join()


class BreederManagerGUI(BaseFrame):

    def __init__(self, breeder_manager: BreederManager, config: Config, master, controller) -> None:
        super().__init__(master=master, controller=controller)
        
        self.config = config
        self.init_gui()
        self.breeder_manager = breeder_manager

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text="Press F1 to toggle")
        instructions_label.pack(padx=20, pady=20)

    def destroy_gui(self):
        self.breeder_manager.destroy_loop()
        super().destroy()
        print("BreederManager destroyed")