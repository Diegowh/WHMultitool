import asyncio
from typing import TYPE_CHECKING

from src.components.windows.magic_f_gui import MagicFGUI
from src.controllers.service import Service
from src.utils import player_actions as pa
from src.utils.screen_manager import (
    StructureInventoryCoordinates,
    PlayerInventoryCoordinates
)

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from src.config.config import Config
    from src.controllers.app_controller import AppController


class MagicF(Service):

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
            gui=MagicFGUI,
            supress_hotkey=False
        )
        
        self.options = self.task_manager.app_config.magic_f_options
        self.first_dump_loop = True
        self.first_craft_loop = True
        super().init_gui()

    async def on_toggle_key(self):
        selected_option = self.gui.selected_option.get()
        
        if selected_option == "dumper":
            await self._dumper_task()
        elif selected_option == "crafter":
            await self._crafter_task()
        elif selected_option == "veggies":
            await self._veggies_task()
        else:
            await self._retrieve_task(item=selected_option)

    async def _veggies_task(self):
        self.task_manager.repetitive_task = False
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.TRANSFER_ALL,
            pre_delay=self.service_config.load_inventory_waiting_time,
            post_delay=self.service_config.transfer_all_waiting_time
        )
        
        await pa.move_cursor_and_click(
            PlayerInventoryCoordinates.TRANSFER_ALL,
            post_delay=self.service_config.transfer_all_waiting_time
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.CLOSE
        )

    async def _dumper_task(self):
        item = self.gui.entries['Dumper'].get()

        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.SEARCH_BAR,
            pre_delay=self.service_config.load_inventory_waiting_time
        )
        await pa.type_text(
            text=item,
            post_delay=self.service_config.after_type_text_waiting_time
        )
        
        inventory_slots = [
            StructureInventoryCoordinates.SLOT1,
            StructureInventoryCoordinates.SLOT2,
            StructureInventoryCoordinates.SLOT3,
            StructureInventoryCoordinates.SLOT7,
            StructureInventoryCoordinates.SLOT8,
            StructureInventoryCoordinates.SLOT9
        ]
        
        while True:
            for slot in inventory_slots:
                await pa.move_cursor_and_click(slot, post_delay=0)
                for _ in range(5):
                    await pa.pop_item(post_delay=0)

    async def _crafter_task(self):
        
        if self.first_craft_loop:
            item = self.gui.entries['Crafter'].get()
            await pa.move_cursor_and_click(
                StructureInventoryCoordinates.SEARCH_BAR,
                pre_delay=self.service_config.load_inventory_waiting_time
            )
            await pa.type_text(
                text=item,
                post_delay=self.service_config.after_type_text_waiting_time
            )
            self.first_craft_loop = False

        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.SLOT1,
        )
        for _ in range(10):
            await pa.craft_all()
        
        await asyncio.sleep(self.service_config.autocraft_interval_time)
        
    async def _retrieve_task(self, item: str):
        
        self.task_manager.repetitive_task = False
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.SEARCH_BAR,
            pre_delay=self.service_config.load_inventory_waiting_time
        )
        
        await pa.type_text(
            text=item,
            post_delay=self.service_config.after_type_text_waiting_time
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.TRANSFER_ALL,
        )
        
        await pa.move_cursor_and_click(
            StructureInventoryCoordinates.CLOSE
        )
        