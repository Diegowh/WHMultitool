import asyncio
from threading import Thread
import time
from abc import ABC, abstractmethod

class BaseTaskManager(ABC):
    """
    This is a base class for task managers. It provides a basic structure for managing tasks in a separate thread.
    """
    def __init__(self) -> None:
        # Initialize here the attributes to keep them trackable
        self.task = None
        self.loop = None
        self.thread = None
        self.task_running = False


    @abstractmethod
    def _task_routine(self) -> None:
        pass    

    def start_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        """Starts the asyncio loop in a separate thread.

        Args:
            loop (asyncio.AbstractEventLoop): The asyncio loop to start.
        """
        asyncio.set_event_loop(loop)
        loop.run_forever()
        print("TaskManager loop started")
    
    def start_thread(self) -> None:
        """Starts the thread for the asyncio loop.
        """
        self.thread = Thread(target=self.start_loop, args=(self.loop,))
        self.thread.start()
        print("Thread started")
        
    def start_task(self) -> None:
        """Starts the task coroutine in the asyncio loop.
        """
        assert not self.task_running
        self.loop = asyncio.new_event_loop()
        self.start_thread()
        self.task_running = True
        self.loop.call_soon_threadsafe(self._start_task_coroutine)
        print("Task started")
    
    def _start_task_coroutine(self) -> None:
        """Creates the task coroutine in the asyncio loop.
        """
        self.task = asyncio.create_task(self.run_task())
        print("Task coroutine started")
    
    def stop_task(self) -> None:
        """Stops the task coroutine in the asyncio loop.
        """
        if self.task_running:
            self.task_running = False
            if self.task is not None:
                self.loop.call_soon_threadsafe(self._stop_task_coroutine)
                print("Task stopped")
    
    def _stop_task_coroutine(self) -> None:
        """Cancels and destroys the task coroutine in the asyncio loop.
        """
        self.task.cancel()
        self.destroy_loop()
        print("Task coroutine stopped")

    def toggle_task(self) -> None:
        """Toggles the task coroutine on and off.
        """
        if self.task_running:
            self.stop_task()
            print("Task toggled off")
        elif self.task is None or self.task.done():
            self.start_task()
            print("Task toggled on")

    async def run_task(self) -> None:
        """Method to run the task coroutine.
        """
        try:
            while self.task_running:
                print("Running task...")
                self._task_routine()
            print("Task finished")
        except Exception as e:
            print(f"Error: {e}")
            self.task_running = False

    def _task_routine(self) -> None:
        """The main task routine to be implemented in the subclass.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    def destroy_loop(self) -> None:
        """Destroys the asyncio loop and the thread.
        """
        print("Destroying TaskManager...")
        self.loop.call_soon_threadsafe(self.loop.stop)
        while self.loop.is_running():
            time.sleep(0.1)
        self.loop.close()
        self.thread.join()