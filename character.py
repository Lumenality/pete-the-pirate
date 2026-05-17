from enum import Enum
from colors import Colors

MAX_LEVEL = 10

class PlayerClasses(Enum):
    PIRATE = 'Pirate'

class Character():
    def __init__(self,name,level = 1,character_class = PlayerClasses.PIRATE.value):
        self.name = name
        self.level = level
        self.character_class = character_class
        self.inventory = None
    
    def __repr__(self):
        return (f"{Colors.OKBLUE}{self.name} is a level {self.level} {self.character_class}{Colors.ENDC}")