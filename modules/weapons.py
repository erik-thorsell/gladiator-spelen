class Weapon:
    def __init__(self, attack, speed, name):
        self.attack = attack
        self.speed = speed
        self.name = name


weapons = {
    "sword": Weapon(10, 5, "svärd"),
    "axe": Weapon(15, 3, "yxa"),
    "spear": Weapon(12, 4, "spjut"),
    "bow": Weapon(8, 6, "båge"),
    "dagger": Weapon(7, 7, "kniv"),
    "hands": Weapon(4, 8, "händer")
}