from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controllers.service import Service


class ServiceGUI(ABC):

    def __init__(
        self,
        service_controller: 'Service',
        master,
        app_controller
    ) -> None:
        self.app_controller = app_controller
        self.service_controller = service_controller
        self.config = self.service_controller.service_config
        self.init_gui()

    @abstractmethod
    def init_gui(self):
        ...

    @abstractmethod
    def destroy_gui(self):
        ...
