from enum import Enum
from colors import Colors
from game.characters.character import Character
from constants import MAX_LEVEL

class PlayerClasses(Enum):
    PIRATE = 'Pirate'

class Player(Character):
    def __init__(self,name,level = 1,character_class = PlayerClasses.PIRATE.value):
        super().__init__(name,level)
        self.character_class = character_class
        self.inventory = None
    
    def __repr__(self):
        return (f"{Colors.OKBLUE}{self.name} is a level {self.level} {self.character_class}{Colors.ENDC}")