from typing import TYPE_CHECKING, Type
from src.config.config import load_service
from src.controllers.base_task_manager import BaseTaskManager
from abc import ABC, abstractmethod


if TYPE_CHECKING:
    import asyncio
    from src.config.config import Config
    from src.controllers.app_controller import AppController
    from src.components.frames.base_frame import BaseFrame


class Service(ABC):
    """Represents a Service"""

    def __init__(
        self,
        loop: 'asyncio.AbstractEventLoop',
        config: 'Config',
        master,
        app_controller: 'AppController',
        gui: Type['BaseFrame'],
        supress_hotkey: bool = True,
    ) -> None:
        self.master = master
        self.app_controller = app_controller
        self.gui_class = gui
        self.service_config = load_service(self.__class__.__name__.upper())

        self.toggle_key = self.service_config.toggle_key
        self.task_manager = BaseTaskManager(
            loop=loop,
            config=config,
            app_controller=self.app_controller,
            service_actions=self.on_toggle_key
        )
        self.task_manager.register_hotkey(self.toggle_key, supress=supress_hotkey)
        self.gui = None

    @abstractmethod
    async def on_toggle_key(self):
        ...

    def init_gui(self):
        self.gui = self.gui_class(
            service_controller=self,
            master=self.master,
            app_controller=self.app_controller,
        )
