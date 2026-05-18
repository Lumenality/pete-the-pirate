from enum import Enum
from colors import Colors
from game.characters.character import Character
from constants import MAX_LEVEL


class Enemy(Character):
    def __init__(self,name,level = 1):
        super().__init__(name,level)
    
    def __repr__(self):
        return (f"{Colors.OKBLUE}{self.name} is a level {self.level} {self.character_class}{Colors.ENDC}")