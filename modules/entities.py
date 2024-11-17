from modules.weapons import weapons
from modules.names import generate_name
import copy

default_inventory = {
    "weapon": weapons["hands"],
    "shield": False
    }

def Entity(is_an_animal = False): # skapar en spelare eller ett djur beroende på om is_an_animal är True eller False
    return Animal() if is_an_animal else Player()
class Player:
    def __init__(self):
        self.name = generate_name() # skapar ett slumpmässigt namn, används bara för motståndaren
        self.health = 100
        self.inventory = copy.deepcopy(default_inventory) # kopierar default_inventory för att undvika att alla spelare delar samma inventory
        self.protected = False # används för skölden
        self.skilled = False # ger spelaren extra skada i strid med ett visst vapen
        self.gender = "Male"
        self.priorityNext = False # ger spelaren prioritet att agera först i nästa runda

class Animal:
    def __init__(self):
        self.name = "Tiger"
        self.health = 150
        self.inventory = default_inventory
        self.inventory["weapon"] = weapons["claws"]
        self.protected = False
        self.skilled = False
        self.gender = "djuret"
        self.priorityNext = False