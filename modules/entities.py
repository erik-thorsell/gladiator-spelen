from modules.weapons import weapons
from modules.names import generate_name

default_inventory = {
    "weapon": weapons["hands"],
    "shield": False
    }

def Entity(is_an_animal = False):
    return Animal() if is_an_animal else Player()
class Player:
    def __init__(self, health=50, inventory=default_inventory, protected = False):
        self.name = generate_name()
        self.health = health
        self.inventory = inventory
        self.protected = protected
    
    def is_an_animal(self) -> bool:
        return False

class Animal:
    def __init__(self, health=50, inventory=default_inventory):
        self.name = "Tiger"
        self.health = health
        self.inventory = inventory
    
    def is_an_animal(self) -> bool:
        return True