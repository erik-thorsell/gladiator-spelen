from modules.text import Text
import random
import os
import time

def choices(self, enemy):
    result = []
    result.append(("Attack", attack(self, enemy)))
    result.append(("Run", run(self, enemy)))
    return result

def run(self, enemy):
    text = Text(enemy_name=enemy.name)
    if random.randint(0, 1) == 0:
        print(text.RunSuccess)
        self.health += 10
        print(f"Du lyckades fly från {enemy.name} och lyckades återhämta dig med 10 hälsa. Du har nu {self.health} hälsa.")
        return True
    else:
        print(text.RunFail)
        self.health -= 5
        print(f"{enemy.name} gjorde 5 skada på dig. Du har {self.health} hälsa kvar.")
        return False

def choose_action(self, enemy):
    os.system("cls")
    text = Text(self.name, enemy.name)
    print(text.ChooseAction)
    for index, (action, func) in enumerate(choices(self, enemy)):
        print(f"{index + 1}. {action}")
    choice = int(input("Välj ett alternativ: "))
    if not 1 <= choice <= len(choices(self, enemy)):
        print("Ogiltigt val. Försök igen.")
        time.sleep(3)
        return choose_action(self, enemy)
    return choices(self, enemy)[choice - 1][1]

def attack(self, enemy):
    text = Text(weapon_name=self.weapon.name, enemy_name=enemy.name, damage=self.weapon.attack)
    print(text.Attack)
    enemy.health -= self.weapon.attack
    print(f"{enemy.name} har {enemy.health} hälsa kvar.")