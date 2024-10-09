import colorama

from modules.entities import Character, Animal

colorama.init(autoreset=True)

player = Character('Player', 100, 10, 5, 5)
opponent = Character('Opponent', 100, 10, 5, 5)

print("""
Welcome to the Gladiator Games!

In a world where only the strongest survive, you have been chosen to fight for glory and honor. 
Step into the arena, where the crowd roars and the ground shakes with the clash of steel. 
Your journey begins now, brave warrior. Will you rise to the challenge and become a legend, 
or will you fall like so many before you?

Prepare yourself, for the battle is about to begin. 

Let the games commence! 
""")

print("Choose your attack:")
for key, attack in player.attacks.items():
    print(f"{key}: {attack['name']} (Damage: {attack['damage']}, Courage: {attack['courage']})")

choice = input("Enter the number of your chosen attack: ")

if choice in player.attacks:
    player.attack(opponent, choice)
else:
    print("Invalid choice. Please select a valid attack.")


player = Character('Player', 100, 10, 5, 5)

print(colorama.Fore.RED + 'some red text')