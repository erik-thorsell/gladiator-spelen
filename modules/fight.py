from modules.text import Text
from modules.weapons import weapons
from modules.utils import clear_screen
from random import randint, choice
from time import sleep
from os import _exit

def enemy_attack(self, player):
    damage = self.inventory["weapon"].attack
    text = Text(player, self, potential_damage=damage)
    if player.protected:
        damage /= 2
    player.health -= damage
    print(text.enemy_attacks)

def attack(self, enemy):
    text = Text(self, enemy)
    enemy.health -= self.inventory["weapon"].attack
    print(text.attack)

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
    
def steal_weapon(self, enemy) -> None:
    text = Text(self, enemy)
    self.inventory["weapon"] = enemy.inventory["weapon"]
    enemy.inventory["weapon"] = weapons["hands"]
    print(text.steal_weapon)

def open_box(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.open_box)
    new_weapon = choice(list(weapons.values()))
    if new_weapon == "a shield.":
        self.inventory["shield"] = True
        print(text.found_shield)
    else:
        self.inventory["weapon"] = new_weapon
        print(text.found_weapon)

def enemy_open_box(self, player) -> None:
    text = Text(player, self)
    print(text.enemy_open_box)
    new_weapon = choice(list(weapons.values()))
    if new_weapon == "a shield.":
        self.inventory["shield"] = True
        print(text.enemy_found_shield)
    else:
        self.inventory["weapon"] = new_weapon
        print(text.enemy_found_weapon)

def defend(self, enemy) -> None:
    text = Text(self, enemy)
    if not self.protected:
        self.protected = True
        print(text.defend)
    else:
        print(text.already_protected)

def give_up(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.give_up)
    sleep(3)
    clear_screen()
    print(text.loss)
    sleep(5)
    _exit(0)


def choices(player, enemy) -> list:
    result = []
    result.append(("Attackera", attack))
    result.append(("Spring", run))
    if player.inventory["shield"]:
        result.append(("Försvara", defend))
    if randint(0, 3) == 1 and not player.inventory["shield"]:
        result.append(("Öppna låda", open_box))
    if randint(0, 5) == 1 and enemy.inventory["weapon"] != weapons["hands"]:
        result.append(("Stjäl vapen", steal_weapon))
    result.append(("Ge upp", give_up))
    return result

def choose_action(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.choose_action)
    available_choices = choices(self, enemy)
    for index, (action, func) in enumerate(available_choices):
        print(f"{index + 1}. {action}")
    print("")
    print(text.list_stats)
    print("")

    choice = input(text.choose_option)
    if not choice.isdigit() or not 1 <= int(choice) <= len(available_choices):
        print(text.wrong_error)
        sleep(3)
        clear_screen()
        return choose_action(self, enemy)
    clear_screen()
    return available_choices[int(choice) - 1][1](self, enemy)

