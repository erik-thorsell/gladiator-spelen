class Character:
    def __init__(self, name, health, strength, defense, agility) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.attacks = {
            '1': {'name': 'Slash', 'damage': 10, 'courage': 1},
            '2': {'name': 'Thrust', 'damage': 15, 'courage': 3},
            '3': {'name': 'Strike', 'damage': 20, 'courage': 5}
        }

    def attack(self, target, attack_choice) -> None:
        damage = self.strength - target.defense
        target.health -= damage
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def __str__(self):
        return self.name
    
class Animal:
    def __init__(self, name, health, strength, defense, agility):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.defense = defense

    def attack(self, target):
        damage = self.strength - target.defense
        target.health -= damage

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return self.name