class Weapon:
    def __init__(self, attack, speed, name):
        self.attack = attack
        self.speed = speed
        self.name = name


weapons = {
    "sword": Weapon(10, 5, "Sword"),
    "axe": Weapon(15, 3, "Axe"),
    "spear": Weapon(12, 4, "Spear"),
    "bow": Weapon(8, 6, "Bow"),
    "dagger": Weapon(7, 7, "Dagger"),
    "hands": Weapon(4, 8, "Hands")
}