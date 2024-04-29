import asyncio
from player_actions import *
from screen_manager import (
    PlayerInventoryCoordinates,
    StructureInventoryCoordinates,
    ScreenCoordinates,
)
import tkinter as tk
from threading import Thread
import keyboard

class BreederManager:
    
    def __init__(self) -> None:
        self.autoeggdrop_task = None
        self.loop = asyncio.new_event_loop()
        self.thread = Thread(target=self.start_loop, args=(self.loop,))
        self.thread.start()
        self.autoeggdrop_running = False
        keyboard.register_hotkey('f1', self.toggle_autoeggdrop, suppress=True)
        
        self.gui = BreederManagerGUI(breeder_manager=self)
        self.gui.mainloop()

    def stop_loop(self):
        for task in asyncio.all_tasks(self.loop):
            task.cancel()
        self.loop.stop()
        if self.thread.is_alive():
            self.thread.join()

    def start_autoeggdrop(self):
        if not self.autoeggdrop_running:
            self.autoeggdrop_running = True
            self.loop.call_soon_threadsafe(self._start_autoeggdrop_coroutine)
            print("Auto-eggdrop started")

    def _start_autoeggdrop_coroutine(self):
        self.autoeggdrop_task = asyncio.create_task(self.run_autoeggdrop())

    def stop_autoeggdrop(self):
        if self.autoeggdrop_running:
            self.autoeggdrop_running = False
            if self.autoeggdrop_task is not None:
                self.loop.call_soon_threadsafe(self._stop_autoeggdrop_coroutine)
            print("Auto-eggdrop stopped")

    def _stop_autoeggdrop_coroutine(self):
        self.autoeggdrop_task.cancel()

    async def run_autoeggdrop(self):
        try:
            while self.autoeggdrop_running:
                await self._autoeggdrop_routine()
        except Exception as e:
            print(f"Error: {e}")
            self.autoeggdrop_running = False

    def toggle_autoeggdrop(self, event=None):
        if self.autoeggdrop_running:
            self.stop_autoeggdrop()
        else:
            self.start_autoeggdrop()
    
    async def _autoeggdrop_routine(self):
        while self.autoeggdrop_running:
            
            open_inventory()
            move_cursor_and_click(location=PlayerInventoryCoordinates.SEARCH_BAR)
            type_text(text="fertilized egg", post_delay=0.2)
            move_cursor_and_click(location=PlayerInventoryCoordinates.FIRST_SLOT,)
            pop_item()
            close_inventory()
            move(direction=MoveDirection.LEFT, prev_delay=0.3)

    def start_loop(self, loop: asyncio.AbstractEventLoop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def destroy(self):
        print("Destroying BreederManager...")
        if self.autoeggdrop_task is not None:
            self.loop.call_soon_threadsafe(self.loop.stop)
        while self.loop.is_running():
            time.sleep(0.1)
        self.loop.close()
        self.thread.join()


class BreederManagerGUI(tk.Tk):

    def __init__(self, breeder_manager: BreederManager) -> None:
        super().__init__()
        self.geometry("200x300")
        self.init_gui()
        self.breeder_manager = breeder_manager

    def init_gui(self):
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text="Press F1 to toggle")
        instructions_label.pack(padx=20, pady=20)

    def destroy(self):
        self.breeder_manager.destroy()
        super().destroy()
        print("BreederManager destroyed")



if __name__ == "__main__":
    bm = BreederManager()
