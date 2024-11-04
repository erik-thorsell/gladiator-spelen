from modules.entities import Player
from modules.text import Text
from modules.fight import choose_action, enemy_attack
from time import time, sleep
from os import system
from math import floor

start = time()
time_limit = 300

system("cls")
player = Player()
enemy = Player()

text = Text(player, enemy)
print(text.start)
# sleep(3)
print(text.welcome)
# sleep(5)
print(text.battle_begins)
print("")
# sleep(2)
input(text.enter)
players_turn = True
while player.health > 0 and enemy.health > 0:
    system("cls")
    if players_turn == True:
        choose_action(player, enemy)
    else:
        enemy_attack(enemy, player)

    delta = time() - start
    if delta > time_limit:
        print(text.draw)
        break

    new_text = Text(player, enemy, 0, 0, floor(time_limit - delta))
    print(new_text.time_remaining)
    input(text.enter)
    players_turn = not players_turn

if player.health > 0:
    print(text.win)
else:
    print(text.lose)

