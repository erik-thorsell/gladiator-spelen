from modules.entities import Entity
from modules.text import Text
from modules.fight import choose_action, enemy_attack
from modules.events import decide_winner
from modules.utils import clear_screen
from time import time, sleep
from random import randint
from math import floor

start = time()
round_length = 1000

clear_screen()
player = Entity()
enemy = Entity()

text = Text(player, enemy)
print(text.start)
sleep(3)
print(text.welcome)
sleep(5)
print(text.battle_begins)
print("")
sleep(2)
input(text.enter)
players_turn = True
while player.health > 0 and enemy.health > 0:
    clear_screen()
    if players_turn == True:
        if randint(0,50) == 25:
            print(text.animal_appears)
            input(text.enter)
            clear_screen()
            enemy = Entity(True)
        choose_action(player, enemy)
    else:
        enemy_attack(enemy, player)

    delta = time() - start
    if delta > round_length:
        break

    new_text = Text(player, enemy, 0, 0, floor(round_length - delta))
    print("")
    print(new_text.time_remaining)
    print("")
    input(text.enter)
    players_turn = not players_turn

clear_screen()
if delta > round_length:
    print(decide_winner(player, enemy))
elif player.health > 0:
    print(text.win)
else:
    print(text.loss)

