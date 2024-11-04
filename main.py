from modules.entities import Player
from modules.text import Text
from modules.fight import choose_action, enemy_attack
from modules.events import decide_winner
from time import time, sleep
from os import system
from math import floor

start = time()
time_limit = 10

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
        break

    new_text = Text(player, enemy, 0, 0, floor(time_limit - delta))
    print(new_text.time_remaining)
    input(text.enter)
    players_turn = not players_turn

system("cls") 
if delta > time_limit:
    print(decide_winner(player, enemy))
elif player.health > 0:
    print(text.win)
else:
    print(text.loss)

