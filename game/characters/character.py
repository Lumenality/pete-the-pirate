from enum import Enum
from colors import Colors

class Character():
    def __init__(self,name, level = 1):
        self.name = name
        self.level = level
        self.health = 10 * self.level
        self.damage = self.level

    def attack(self,target):
        target.health -= self.damage
        
    def __repr__(self):
        return (f"{Colors.OKBLUE}A level {self.level} {self.name}{Colors.ENDC}")