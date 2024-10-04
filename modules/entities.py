class Character:
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