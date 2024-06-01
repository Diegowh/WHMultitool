"""
Base class for service task managers.
"""


import asyncio
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import keyboard
if TYPE_CHECKING:
    from src.controllers.app_controller import AppController

class BaseTaskManager(ABC):
    """
    Base class for task managers,
    provides a basic structure for managing tasks in a separate thread.
    """
    def __init__(self,
        loop: asyncio.AbstractEventLoop,
        app_controller: 'AppController',
        repetitive_task: bool = True,
    ) -> None:
        
        self.loop = loop
        self.task = None
        self.task_name = self.task.get_name() if self.task is not None else None
        self.task_running = False
        self.first_run = True
        self.app_controller = app_controller
        
        self.repetitive_task = repetitive_task

    @abstractmethod
    async def _task(self) -> None:
        """
        Abstract method repersenting the core task to be performed by a service controller.
        
        This metod is intended to be overridden by subclasses
        to define a sequence of in-game actions.
        
        These actions are specific to the service
        and are executed repeatedly  in a loop while the task is running.
        
        For example, a service controller might define this method
        to automate a series of clicks, cursor movements, and text inputs.
        """

    async def coroutine(self) -> None:
        """Method to encapsulate and control the task coroutine in a loop.
        """
        try:
            self.task_running = True
            while self.task_running:
                print("Running task...")
                await self._task()
    
                # This is a non-blocking call.
                # It's used to give control to the asyncio event loop.
                # Allows other tasks to run before this task continues.
                await asyncio.sleep(0)
    
                if not self.repetitive_task:
                    self.task_running = False
                    break
    
        except asyncio.CancelledError:
            print("Task cancelled")
            self.task_running = False
            self.first_run = True

    def start_task(self) -> None:
        """Starts the task coroutine in the asyncio loop.
        
        Args:
            coro (asyncio.Coroutine): The coroutine to start.
        """
        if self.app_controller.is_ark_in_focus:
            self.task = self.loop.create_task(self.coroutine())
            self.task_running = True
            print("Task started")

    def stop_task(self) -> None:
        """Stops the task coroutine in the asyncio loop.
        """
        if self.task is not None:
            self.task.cancel()
            print("Task stopped")

    def toggle_task(self) -> None:
        """Toggles the task coroutine on and off.
        """
        if self.task_running:
            self.stop_task()
            self.task_running = False
            self.first_run = True
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
        print("Unregistered all hotkeys")

    def register_hotkey(self, hotkey, supress: bool = True):
        
        keyboard.register_hotkey(hotkey, self.toggle_task, suppress=supress)