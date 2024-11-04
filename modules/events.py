from modules.text import Text
from random import randint
from time import sleep

def decide_winner(player, enemy) -> str:
    text = Text(player, enemy)
    print(text.time_is_out)
    sleep(2)
    emperor = randint(0, 1)
    if emperor == 0: # emperor is not present
        if player.health > enemy.health:
            return text.win
        elif player.health < enemy.health:
            return text.loss
        else:
            text.draw
    else: # emperor is present
        print(text.emperor)
        sleep(3)
        if player.health > enemy.health:
            return text.win_emperor
        elif player.health < enemy.health:
            return text.loss_emperor
        else:
            text.draw_emperor