from modules.entities import Player
from modules.text import Text
from modules.fight import choose_action
import time
import os
import math

dev_mode = 0

def sleep(num):
    time.sleep(num * dev_mode)

start = time.time()
time_limit = 300

player = Player()
enemy = Player()
os.system("cls")
text = Text(player, enemy)
print(text.Start)
sleep(3)
print(text.Welcome)
sleep(5)
print(text.BattleBegins)
sleep(2)
print("")
input("Tryck på enter för att fortsätta...")
turn = True
while player.health > 0 and enemy.health > 0:
    if turn == True:
        choose_action(player, enemy)
    else:
        choose_action(enemy, player, "1")
    asd = time.time() - start
    if asd > time_limit:
        print("Tiden har gått ut. Striden slutar oavgjort.")
        break
    print(f"{math.floor(time_limit - asd)} sekunder återstår av striden.")
    input("Tryck på enter för att fortsätta...")
    turn = not turn

if player.health > 0:
    print(text.End)
else:
    print(text.Lose)

