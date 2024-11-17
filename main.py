
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
input(text.enter)

# ta reda på spelarens namn och kön
player.name = "" # sätt spelarens namn till en tom sträng
while player.name == "": # loopa tills spelaren har skrivit in ett namn
    name = input("Först och främst, vad heter du? ")
    if name == "": # om spelaren inte skriver in något, skriv ut en varning
        print("Du måste skriva in ett namn!")
        input(text.enter)
        clear_screen()
    else: # annars sätt spelarens namn till det som spelaren skrev in
        player.name = name
print(f"Välkommen {player.name}!")
sleep(1)
clear_screen()

player.gender = "" # sätt spelarens kön till en tom sträng
while player.gender == "": # loopa tills spelaren har valt ett kön
    print("Vilket kön är du?")
    print("1. Man")
    print("2. Kvinna")
    print("3. Icke-binär")
    gender_choice = input("Välj kön: (1/2/3) ")
    if gender_choice == "1":
        player.gender = "mannen"
        print("Du är man.")
    elif gender_choice == "2":
        player.gender = "kvinnan"
        print("Du är kvinna.")
    elif gender_choice == "3":
        player.gender = "icke-binära"
        print("Du är icke-binär.")
    else: # om spelaren inte väljer ett giltigt alternativ, skriv ut en varning
        print("Du måste välja ett giltigt alternativ!")
        input(text.enter)
        clear_screen()
sleep(1)
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
input(text.enter)
clear_screen()

#skriv ut välkomsttexten och börja striden
text = Text(player, enemy)
print(text.welcome)
print(text.battle_begins)
print("")
input(text.enter)


players_turn = True
while player.health > 0 and enemy.health > 0: # loopa tills en av spelarna har 0 hälsa eller tiden tar slut
    # try: # try för att se till att spelet aldrig visar felmeddelanden
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

            elif randint(0,3) == 1 and not enemy.inventory["weapon"].name == "yxa": # annars är det 30% chans att motståndaren öppnar en låda, om hen inte redan har det bästa vapnet
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
    # except KeyboardInterrupt:
    #     _exit(0)
    # except:
    #     # ge spelaren en andra chans att göra sitt val om något går fel
    #     players_turn = True
    #     print(text.oops) # med en liten text som ber om ursäkt
    #     sleep(2)

clear_screen()

# om tiden har gått ut, låt publiken bestämma vinnaren
if delta > round_length:
    print(decide_winner(player, enemy))
elif player.health > 0: # annars om spelaren har mer hälsa än motståndaren, låt spelaren vinna
    print(text.win)
    print(text.strongest)
else: # annars låt motståndaren vinna
    print(text.loss)

