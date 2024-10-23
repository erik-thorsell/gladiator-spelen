from modules.text import Text
import random
import os
import time

def choices() -> list:
    result = []
    result.append(("Attack", attack))
    result.append(("Run", run))
    return result

def run(self, enemy) -> bool:
    potential_damage = random.randint(1, 8)
    potential_health = random.randint(1, 10)
    text = Text(self, enemy, potential_damage=potential_damage, potential_health=potential_health)
    if random.randint(0, 1) == 0 and potential_health + self.health < 100:
        print(text.RunSuccess)
        self.health += potential_health
        return True
    else:
        print(text.RunFail)
        self.health -= potential_damage
        return False

def choose_action(self, enemy, prechosen: str = None):
    os.system("cls")
    text = Text(self, enemy)
    print(text.ChooseAction)
    for index, (action, func) in enumerate(choices()):
        print(f"{index + 1}. {action}")
    print(text.ListStats)

    choice = prechosen or input(text.ChooseOption)
    if not choice.isdigit() or not 1 <= int(choice) <= len(choices()):
        print(text.WrongError)
        time.sleep(3)
        return choose_action(self, enemy)
    return choices()[int(choice) - 1][1](self, enemy)

def attack(self, enemy):
    text = Text(self, enemy)
    enemy.health -= self.weapon.attack
    print(text.Attack)