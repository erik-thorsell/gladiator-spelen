from modules.weapons import weapons
from modules.names import generate_name

class Player:
    def __init__(self, name=generate_name(), health=100, weapon=weapons["hands"]):
        self.name = name
        self.health = health
        self.weapon = weapon