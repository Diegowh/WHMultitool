import asyncio
from typing import TYPE_CHECKING

from src.components.windows.magic_f_gui import MagicFGUI
if TYPE_CHECKING:
    from config.config import Config

class MagicF:
    
    def __init__(self,
        loop: asyncio.AbstractEventLoop,
        config: 'Config',
        master,
        controller,
    ):
        self.loop = loop
        self.config = config
        self.gui = MagicFGUI(
            magic_f=self,
            master=master,
            controller=controller
            
        )
    
    def __name__(self):
       return "Magic-F" 
   