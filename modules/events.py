from modules.text import Text
from random import randint
from time import sleep

# låter publiken eller kejsaren bestämma vinnaren om tiden tar slut
def decide_winner(player, enemy) -> str:
    text = Text(player, enemy)
    print(text.time_is_out)
    sleep(2)
    emperor = randint(0, 1) # 50% chans att kejsaren är närvarande
    if emperor == 0: # kejsaren är inte närvarande!
        if player.health > enemy.health: #om spelaren har mer hälsa, får hen vinna.
            return text.win
        elif player.health < enemy.health: #om hen däremot har mindre, låt hen förlora
            return text.loss
        else: 
            return text.draw # annars blir det oavgjort
    else: # kejsaren är närvarande!
        print(text.emperor)
        sleep(3)
        #samma grej här fast texten byts ut
        if player.health > enemy.health:
            return text.win_emperor
        elif player.health < enemy.health:
            return text.loss_emperor
        else:
            text.draw_emperor