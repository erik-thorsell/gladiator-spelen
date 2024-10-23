from modules.entities import Player
from modules.text import Text
from modules.fight import choose_action
import time
import os

dev_mode = 0

def sleep(num):
    time.sleep(num * dev_mode)

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
    input("Tryck på enter för att fortsätta...")
    turn = not turn

if player.health > 0:
    print(text.End)
else:
    print(text.Lose)

