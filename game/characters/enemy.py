from enum import Enum
from colors import Colors
from game.characters.character import Character
from constants import MAX_LEVEL


class Enemy(Character):
    def __init__(self,name,level = 1):
        super().__init__(name,level)
        