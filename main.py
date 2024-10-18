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
text = Text(player.name)
print(text.Start)
sleep(3)
print(text.Welcome)
sleep(5)
print(text.BattleBegins)
sleep(2)
choose_action(player, enemy)

