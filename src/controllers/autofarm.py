
import asyncio
from typing import TYPE_CHECKING
from src.controllers.base_task_manager import BaseTaskManager
from src.components.windows.autofarm_gui import AutoFarmGUI
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    StructureInventoryCoordinates
)
from src.config.config import load_service

if TYPE_CHECKING:
    from src.config.config import Config
    from src.controllers.app_controller import AppController

RESOURCES = {
    "Stone": "Stone",
    "Wood": "Wood",
    "Thatch": "Thatch",
    "Crystal": "Crystal",
    "Berries": "Berr",
    "Rare Flower": "Flow",
    "Rare Mushroom": "Mushr",
    "Flint": "Flint",
    "Metal": "Metal",
    "Obsidian": "Obsi",
    "Raw": "Raw",
    "Hide": "Hide",
    "Fiber": "Fiber",
    "Chitin": "Chitin",
    "Seed": "Seed",
    "Amarberry": "Amar",
    "Azulberry": "Azul",
    "Cianberry": "Cian",
    "Magenberry": "Magen",
    "Mejoberry": "Mejo",
    "Narcoberry": "Narcob",
    "Stimberry": "Stimb",
    "Verdeberry": "Verdeb",
    "Tintoberry": "Tinto",
    "Pelt": "Pelt",
    "Primitive": "Prim"
}


class AutoFarm(BaseTaskManager):

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller: 'AppController'
    ):
    
        super().__init__(loop=loop, app_controller=app_controller)
        self.app_config = config
        self.service_config = load_service(self.__class__.__name__.upper())
        self.toggle_key = self.service_config.toggle_key
        
        self.register_hotkey(self.toggle_key, supress=False)
        
        self.resources = RESOURCES
        self.gui = AutoFarmGUI(
            autofarm=self,
            master=master,
            app_controller=app_controller
        )

    async def _task(self):
        
        self.repetitive_task = False
        
        selected_resources = self.gui.get_selected_resources()
        selected_values = [self.resources[resource] for resource in selected_resources]
        
        for resource in selected_values:
            await self.drop_resource(resource)
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.CLOSE
        )
        
    async def drop_resource(self, resource):
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.SEARCH_BAR,
            pre_delay=self.service_config.load_inventory_waiting_time
        )
        await pa.type_text(
            text=resource,
            post_delay=self.service_config.after_type_text_waiting_time
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.DROP_ALL,
        )
        