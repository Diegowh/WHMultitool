
import asyncio
from typing import TYPE_CHECKING

from src.components.windows.autofarm_gui import AutoFarmGUI
from src.controllers.service import Service
from src.utils import player_actions as pa
from src.utils.screen_manager import StructureInventoryCoordinates

if TYPE_CHECKING:
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class AutoFarm(Service):

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        app_controller: 'AppController'
    ) -> None:
        super().__init__(
            loop=loop,
            config=config,
            master=master,
            app_controller=app_controller,
            gui=AutoFarmGUI,
            supress_hotkey=False
        )
        self.resources = self.task_manager.app_config.autofarm_resources  # TODO: Darle un par de vueltas a esto
        super().init_gui()

    async def on_toggle_key(self):
        
        self.task_manager.repetitive_task = False
        
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
        