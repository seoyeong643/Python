# File name: battlegame.py
# Game that allows users to select a type of character... and they battle a Dragon.
# Includes if statements, while loops, printing and input

from random import randint

"""
Step 1) Create three characters with type, health, and damage.

elf = "Elf"
elf_hp = 20
elf_dmg = 15

Human
Troll

Step 2) Create a dragon with type, health, and damage

dragon = "Red Dragon"
dragon_hp = 50
dragon_dmg = 60

step 3) Ask the user to choose which character they want to use

Step 4) Have the user battle the dragon
"""

#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Dragon%20Battle
print("""
________                                       __________         __    __  .__          
\______ \____________     ____   ____   ____   \______   \_____ _/  |__/  |_|  |   ____  
 |    |  \_  __ \__  \   / ___\ /  _ \ /    \   |    |  _/\__  \\\   __\   __\  | _/ __ \ 
 |    `   \  | \// __ \_/ /_/  >  <_> )   |  \  |    |   \ / __ \|  |  |  | |  |_\  ___/ 
/_______  /__|  (____  /\___  / \____/|___|  /  |______  /(____  /__|  |__| |____/\___  >
        \/           \//_____/             \/          \/      \/                     \/ 

""")

wizard = "Wizard"
wizard_hp = 70
wizard_dmg = 150

elf = "Elf"
elf_hp = 100
elf_dmg = 100

human = "Human"
human_hp = 150
human_dmg = 20

"""
troll = "Troll"
troll_hp = 45
troll_dmg = 35
"""

dragon = "Red Dragon"
dragon_hp = 300
dragon_dmg = 50

character = ""
character_hp = 0
character_dmg = 0

while True:
    print(f"1) {wizard}")
    print(f"2) {elf}")
    print(f"3) {human}")

    choice = input("Choose your character (1:wizard, 2:elf, 3:human): ")

    if choice == "1" or choice == "wizard":
        character = wizard
        character_hp = wizard_hp
        character_dmg = wizard_dmg
        break

    elif choice == "2" or choice == "elf":
        character = elf
        character_hp = elf_hp
        character_dmg = elf_dmg
        break

    elif choice == "3" or choice == "human":
        character = human
        character_hp = human_hp
        character_dmg = human_dmg
        break

    else:
        print("Unknown character\n")

print(f"""

Great selection for Dragon Battle. 
Your character selection is: {character}
Your {character}'s health is: {character_hp}
Your {character}'s damage is: {character_dmg}

""")

while True:
    """
    print("Today's event will be Death by Dragon! ")
    print(f"In the left corner we have the {character} who's life will soon be ended.")
    print(f"In the right corner, we have the {dragon} who is undefeated.")
    print("The crown cheers... AHHHHHH\n")
    """

    real_character_damage = randint(0, character_dmg)

    print(f"{character} attacks for {real_character_damage}.")
    print(f"{dragon}'s health is at {dragon_hp} and takes {real_character_damage}")
    dragon_hp -= real_character_damage

    if dragon_hp < 0:
        print("The dragon has turned to ash")
        dragon_hp = 0

    print(f"{dragon}'s health is now at: {dragon_hp}")

    if dragon_hp <= 0:
        print(f"The {dragon} has lost the battle")
        break

    input("\nPRESS ENTER TO MOVE ON...\n")

    real_dragon_damage = randint(0, dragon_dmg)

    print(f"{dragon} attacks for {real_dragon_damage}.")
    print(f"{character}'s health is at {character_hp} and takes {real_dragon_damage}")

    character_hp -= real_dragon_damage

    if character_hp < 0:
        print("Your character has turned to ash...")
        character_hp = 0

    print(f"{character}'s health is now at: {character_hp}")

    input("\nPRESS ENTER TO MOVE ON...\n")

    if character_hp <= 0:
        print(f"The {character} lost the battle")
        break

    """
    print("Your game has ended.")
    new_game = input("Would you like to play again? (Y/N) ")
    # Yes, No
    if new_game[0].lower() == "n":
        break
    print()
    """

print("Your game has ended. Goodbye")
