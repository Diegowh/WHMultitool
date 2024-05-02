import asyncio
from threading import Thread
import time
from abc import ABC, abstractmethod

import keyboard

class BaseTaskManager(ABC):
    """
    This is a base class for task managers. It provides a basic structure for managing tasks in a separate thread.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
        self.task = None
        self.task_name = self.task.get_name() if self.task is not None else None
        self.task_running = False

    @abstractmethod
    async def _task(self) -> None:
        pass
    
    async def coroutine(self) -> None:
        """Method to encapsulate the task coroutine.
        """
        try:
            while self.task_running:
                print("Running task...")
                await self._task()
                
                # This is a non-blocking call.
                # It's used to give control to the asyncio event loop.
                # Allows other tasks to run before this task continues.
                await asyncio.sleep(0)
        
        except asyncio.CancelledError:
            print("Task cancelled")
            self.task_running = False
        # finally:
        #     print("Task stopped")
        #     self.task_running = False
    
    def start_task(self) -> None:
        """Starts the task coroutine in the asyncio loop.
        
        Args:
            coro (asyncio.Coroutine): The coroutine to start.
        """
        self.task = self.loop.create_task(self.coroutine())
        self.task_running = True
        print(f"Task started")
    
    def stop_task(self) -> None:
        """Stops the task coroutine in the asyncio loop.
        """
        if self.task is not None:
            self.task.cancel()
            print(f"Task stopped")

    def toggle_task(self) -> None:
        """Toggles the task coroutine on and off.
        """
        if self.task_running:
            self.stop_task()
            print("Task toggled off")
        else:
            self.start_task()
            print("Task toggled on")

    def destroy(self) -> None:
        """Destroys the asyncio loop and the thread.
        """
        print("Destroying TaskManager...")
        if self.task is not None:
            self.loop.call_soon_threadsafe(self.task.cancel)
        
        keyboard.unregister_all_hotkeys()
        print(f"Unregistered all hotkeys")