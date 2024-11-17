
# importera alla moduler som behövs
from modules.text import Text
from modules.weapons import weapons, get_random_weapon
from modules.utils import clear_screen
from random import randint, choice
from time import sleep
from os import _exit


#MOTSTÅNDARENS ATTACK
def enemy_attack(self, player) -> None:
    damage = self.inventory["weapon"].attack # ta basattacken från vapnet
    text = Text(self, player)

    if player.protected: # om spelaren har sin sköld uppe, halvera skadan
        print(text.protected)
        damage /= 2

    if self.skilled: # om motståndaren är särskilt skicklig med sitt vapen, öka skadan med 25%
        damage *= 1.25
        print(text.enemy_attack_skilled)

    player.health -= damage # dra bort skadan från spelarens hälsa
    text = Text(player, self, potential_damage=damage)
    print(text.enemy_attacks)

    #om spelaren är skyddad, 50% chans att skyddet försvinner
    if not player.protected: return
    if randint(0, 2) == 1:
        print(text.stop_defending)
        player.protected = False
    else:
        print(text.continue_defending)

#SPELARENS ATTACK
def attack(self, enemy):

    damage = self.inventory["weapon"].attack # ta basattacken från vapnet
    text = Text(self, enemy)

    if enemy.protected: # om motståndaren har sin sköld uppe, halvera skadan
        damage /= 2
        print(text.enemy_protected)

    if self.skilled: # om spelaren är särskilt skicklig med sitt vapen, öka skadan med 25%
        damage *= 1.25
        print(text.attack_skilled)

    text = Text(self, enemy, potential_damage=damage)
    enemy.health -= damage # dra bort skadan från motståndarens hälsa
    print(text.attack)

    #om motståndaren är skyddad, 50% chans att skyddet försvinner
    if not enemy.protected: return
    if randint(0, 2) == 1:
        enemy.protected = False
        print(text.enemy_stop_defending)
    else:
        print(text.enemy_continue_defending)

#SPELARENS FLYKT
def run(self, enemy) -> bool:
    self.priorityNext = True # spelaren får prioritet att agera först i nästa runda, oavsett vad som händer
    potential_damage = randint(1, 8) # slumpa potentiell skada
    potential_health = randint(1, 10) # slumpa potentiell hälsa

    text = Text(self, enemy, potential_damage=potential_damage, potential_health=potential_health)

    if randint(0, 1) == 0 and potential_health + self.health < 100: # 50% chans att fly och få tillbaka hälsa, ifall spelaren inte skulle få mer än 100 hälsa
        print(text.run_success)
        self.health += potential_health
        return True
    else: # om spelaren inte lyckas fly, dra bort potentiell skada från hälsan
        print(text.run_fail)
        self.health -= potential_damage
        return False
    
#MOTSTÅNDARENS FLYKT
def enemy_run(self, player) -> None:
    #ingen prioritet för motståndaren
    potential_damage = randint(1, 8) # slumpa potentiell skada
    potential_health = randint(1, 10) # slumpa potentiell hälsa

    text = Text(player, self, potential_damage=potential_damage, potential_health=potential_health)

    if randint(0, 1) == 0 and potential_health + self.health < 100: #om motståndaren lyckas fly och inte får mer än 100 hälsa
        print(text.enemy_run_success)
        self.health += potential_health
    else: # om motståndaren inte lyckas fly, dra bort potentiell skada från hälsan
        print(text.enemy_run_fail)
        self.health -= potential_damage
    
#STJÄLA MOTSTÅNDARENS VAPEN
def steal_weapon(self, enemy) -> None:
    text = Text(self, enemy)
    self.inventory["weapon"] = enemy.inventory["weapon"] # byt ut spelarens vapen mot motståndarens
    enemy.inventory["weapon"] = weapons["hands"] # sätt motståndarens vapen till händerna
    enemy.skilled = False # motståndaren är inte längre skicklig
    print(text.steal_weapon)

#ÖPPNA LÅDA
def open_box(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.open_box)
    sleep(1)

    new_weapon = get_random_weapon(self.inventory["weapon"]) # slumpa ett nytt vapen, tar bort vissa vapen som inte ska kunna hittas

    if new_weapon == "a shield.": # om spelaren hittar en sköld
        self.inventory["shield"] = True
        print(text.found_shield)

    else: # annars hittar spelaren ett nytt vapen
        text = Text(self, enemy, weapon=new_weapon)
        print(text.found_weapon)
        sleep(1)

        skilled = False
        # 50% chans att spelaren blir skicklig med sitt nya vapen
        if randint(0, 1) == 1: 
            print(text.skilled)
            skilled = True
        
        #låt spelaren välja om hen vill ta upp vapnet eller inte
        answer = ""
        while True:
            answer = input("Vill du ta upp vapnet? (ja/nej) ").lower()
            if answer == "ja":
                self.inventory["weapon"] = new_weapon
                print(f"Du tog upp {new_weapon.name}.")
                self.skilled = skilled
            elif answer == "nej":
                print("Du lämnade vapnet kvar.")
            if answer == "ja" or answer == "nej":
                break
        

#ÖPPNA LÅDA FÖR MOTSTÅNDAREN
def enemy_open_box(self, player) -> None:
    text = Text(player, self)
    print(text.enemy_open_box)

    new_weapon = get_random_weapon(self.inventory["weapon"]) # slumpa ett nytt vapen, tar bort vissa vapen som inte ska kunna hittas
    if new_weapon == "a shield.":
        self.inventory["shield"] = True
        text = Text(player, self)
        print(text.enemy_found_shield)

    else: # annars hittar motståndaren ett nytt vapen
        self.inventory["weapon"] = new_weapon
        text = Text(player, self)
        print(text.enemy_found_weapon)

        # 50% chans att motståndaren blir skicklig med sitt nya vapen
        if randint(0, 1) == 1:
            print(text.enemy_skilled)
            self.skilled = True

#FÖRSVARA MED SKÖLD
def defend(self, enemy) -> None:
    text = Text(self, enemy)
    if not self.protected: # om spelaren inte redan är skyddad, skydda spelaren
        self.protected = True
        print(text.defend)
    else: # annars om spelaren redan är skyddad, meddela spelaren
        print(text.already_protected)

#GE UPP - AVSLUTA SPELET
def give_up(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.give_up)
    sleep(3)
    clear_screen()
    print(text.loss)
    sleep(5)
    _exit(0)


#VALMÖJLIGHETER FÖR SPELAREN

def choices(player, enemy) -> list: #skapar en lista med alla möjliga val för spelaren
    result = [] # en lista med alla möjliga val
    # varje val är en tuple med en sträng som beskriver vad valet gör och en funktion som utför valet

    #BASVAL
    result.append((f"Attackera | {player.inventory["weapon"].name} - {player.inventory["weapon"].attack *1.25 if player.skilled == True else player.inventory["weapon"].attack} skada{" (skicklig)" if player.skilled == True else ""}", attack))
    result.append(("Spring | 50% chans att förlora eller få tillbaka hälsa", run))


    #EXTRAVVAL
    if player.inventory["shield"]: # om spelaren har en sköld, lägg till försvar som ett val
        result.append((f"Försvara{" [AKTIV]" if player.protected == True else ""} | -50% skada tills skölden tar slut", defend))

    if randint(0, 3) == 1: #30% chans att kunna få ett nytt vapen
        result.append(("Öppna låda | få ett nytt vapen!", open_box))

    if randint(0, 5) == 1 and enemy.inventory["weapon"].name != weapons["hands"].name: # liten chans att kunna stjäla motståndarens vapen, förutsatt att motståndaren har ett annat vapen
        result.append(("Stjäl vapen | ta motståndarens vapen och byt ut det mot ditt eget", steal_weapon))

    result.append(("Ge upp", give_up))
    return result

#VISA VALEN FÖR SPELAREN
def choose_action(self, enemy) -> None:
    text = Text(self, enemy)
    print(text.choose_action)
    available_choices = choices(self, enemy) # få de olika valmöjligheterna
    for index, (action, _) in enumerate(available_choices): #loopa igenom dem och visa dem för spelaren
        print(f"{index + 1}. {action}") # printa det +1 för att göra det mer user friendly
    print("")
    print(text.list_stats)
    print("")

    choice = input(text.choose_option) # läs spelarinput
    if not choice.isdigit() or not 1 <= int(choice) <= len(available_choices): # om valet inte är en siffra eller inte finns i listan, skriv ut felmeddelande och försök igen
        print(text.wrong_error)
        sleep(.5)
        clear_screen()
        return choose_action(self, enemy)
    clear_screen()
    return available_choices[int(choice) - 1][1](self, enemy) # annars, kör funktionen som hör till valet

