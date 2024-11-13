from random import choice
import copy

class Weapon: # skapar ett vapen
    def __init__(self, attack, name):
        self.attack = attack
        self.name = name

def get_random_weapon(current_weapon): # väljer ett slumpmässigt vapen som inte är det nuvarande vapnet eller händer/klor
    newdict = copy.deepcopy(weapons)
    for key, value in weapons.items():
        if value.name == current_weapon.name:
            current_weapon_key = key
            break
    del newdict[current_weapon_key]
    if not current_weapon.name == "händer":
        del newdict["hands"]
    del newdict["claws"]
    return choice(list(newdict.values()))

#definiera alla vapen som finns i spelet
weapons = {
    "sword": Weapon(10, "svärd"),
    "axe": Weapon(15, "yxa"),
    "spear": Weapon(12, "spjut"),
    "bow": Weapon(8, "båge"),
    "dagger": Weapon(7, "kniv"),
    "hands": Weapon(4, "händer"),
    "claws": Weapon(6, "klor"),
    "shield": "a shield."
}