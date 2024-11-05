from modules.weapons import weapons
from modules.names import generate_name
import copy

default_inventory = {
    "weapon": weapons["hands"],
    "shield": False
    }

def Entity(is_an_animal = False):
    return Animal() if is_an_animal else Player()
class Player:
    def __init__(self):
        self.name = generate_name()
        self.health = 100
        self.inventory = copy.deepcopy(default_inventory)
        self.protected = False
        self.skilled = False
    
    def is_an_animal(self) -> bool:
        return False

class Animal:
    def __init__(self):
        self.name = "Tiger"
        self.health = 150
        self.inventory = default_inventory
        self.inventory["weapon"] = weapons["claws"]
    
    def is_an_animal(self) -> bool:
        return True