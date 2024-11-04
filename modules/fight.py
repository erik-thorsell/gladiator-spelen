from modules.text import Text
from random import randint
from os import system
from time import sleep

def choices() -> list:
    result = []
    result.append(("Attackera", attack))
    result.append(("Spring", run))
    return result

def run(self, enemy) -> bool:
    potential_damage = randint(1, 8)
    potential_health = randint(1, 10)
    text = Text(self, enemy, potential_damage=potential_damage, potential_health=potential_health)
    if randint(0, 1) == 0 and potential_health + self.health < 100:
        print(text.run_success)
        self.health += potential_health
        return True
    else:
        print(text.run_fail)
        self.health -= potential_damage
        return False

def choose_action(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.choose_action)
    for index, (action, func) in enumerate(choices()):
        print(f"{index + 1}. {action}")
    print(text.list_stats)

    choice = input(text.choose_option)
    if not choice.isdigit() or not 1 <= int(choice) <= len(choices()):
        print(text.wrong_error)
        sleep(3)
        return choose_action(self, enemy)
    system("cls")
    return choices()[int(choice) - 1][1](self, enemy)

def enemy_attack(self, player):
    text = Text(player, self)
    player.health -= self.weapon.attack
    print(text.enemy_attacks)

def attack(self, enemy):
    text = Text(self, enemy)
    enemy.health -= self.weapon.attack
    print(text.attack)