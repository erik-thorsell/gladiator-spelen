from modules.weapons import weapons
from modules.names import generate_name

class Player:
    def __init__(self, health=50, weapon=weapons["hands"]):
        self.name = generate_name()
        self.health = health
        self.weapon = weapon
    
    def is_an_animal(self) -> bool:
        return False

class Animal:
    def __init__(self, health=50, weapon=weapons["claws"]):
        self.name = "Tiger"
        self.health = health
        self.weapon = weapon
    
    def is_an_animal(self) -> bool:
        return True