
#IMPORTERA ALLA MODULER
from modules.entities import Entity
from modules.text import Text
from modules.fight import choose_action, enemy_attack, enemy_open_box, enemy_run
from modules.events import decide_winner
from modules.utils import clear_screen
from time import time, sleep
from random import randint
from math import floor
from os import _exit

start = time() # starttiden som används för att räkna ut delta
round_length = 1000 # tiden som spelaren har på sig att slåss innan publiken bestämmer vinnaren

clear_screen()

#SKAPA SPELARE OCH MOTSTÅNDARE
player = Entity()
enemy = Entity()

text = Text(player, enemy)
print(text.start)

# ta reda på spelarens namn och kön
name = input("Först och främst, vad heter du? ")
player.name = name
print(f"Välkommen {player.name}!")
sleep(2)
clear_screen()

player.gender = input("Vilket kön är du? ")
print(f"Du är {player.gender}.")
sleep(2)
clear_screen()

# välj svårighetsgrad
print("Vilken svårighetsgrad vill du spela på?")
print("1. Lätt")
print("2. Medel")
print("3. Svår")
difficulty = input("Välj svårighetsgrad: (1/2/3) ")
if difficulty == "2":
    player.health = 80
    enemy.health = 100
elif difficulty == "3":
    player.health = 75
    enemy.health = 125
#skriv ut hälsan för spelaren och motståndaren
print("Din hälsa: ", player.health)
print("Motståndarens hälsa: ", enemy.health)
sleep(2)
clear_screen()

#skriv ut välkomsttexten och börja striden
sleep(1)
text = Text(player, enemy)
print(text.welcome)
sleep(5)
print(text.battle_begins)
print("")
sleep(2)
input(text.enter)


players_turn = True
while player.health > 0 and enemy.health > 0: # loopa tills en av spelarna har 0 hälsa eller tiden tar slut
    try: # try för att se till att spelet aldrig visar felmeddelanden
        clear_screen()
        if players_turn == True or player.priorityNext == True: # om det är spelarens tur
            player.priorityNext = False

            if randint(0,50) == 25: # 2% chans att tigern kommer in i spelet
                print(text.animal_appears)
                input(text.enter)
                clear_screen()
                enemy = Entity(True)

            choose_action(player, enemy) #låt spelaren bestämma vad hen vill göra

        else:

            # om motståndarens sköld är uppe, hen inte är skyddad och 50% chans, få hen att skydda sig.
            if enemy.inventory["shield"] == True and not enemy.protected and randint(0, 1) == 1:
                enemy.protected = True
                print(text.enemy_defend)
                input(text.enter)

            elif randint(0,3) == 1: # annars är det 30% chans att motståndaren öppnar en låda
                enemy_open_box(enemy, player)

            elif enemy.health < 30 and randint(0, 1) == 1: # om motståndaren har mindre än 30 hälsa, 50% chans att hen flyr
                enemy_run(enemy, player)

            else: # annars attackera spelaren
                enemy_attack(enemy, player)

        # ränka ut hur mycket tid som har gått, om tiden som har gått är mer än round_length, bryt loopen och avsluta spelet
        delta = time() - start
        if delta > round_length:
            break

        #skriv ut hur lång tid som är kvar
        new_text = Text(player, enemy, 0, 0, floor(round_length - delta))
        print("")
        print(new_text.time_remaining)
        print("")
        input(text.enter)
        players_turn = not players_turn
    
    #errorhantering
    except KeyboardInterrupt:
        _exit(0)
    except:
        # ge spelaren en andra chans att göra sitt val om något går fel
        players_turn = True
        print(text.oops) # med en liten text som ber om ursäkt
        sleep(2)

clear_screen()

# om tiden har gått ut, låt publiken bestämma vinnaren
if delta > round_length:
    print(decide_winner(player, enemy))
elif player.health > 0: # annars om spelaren har mer hälsa än motståndaren, låt spelaren vinna
    print(text.win)
else: # annars låt motståndaren vinna
    print(text.loss)

