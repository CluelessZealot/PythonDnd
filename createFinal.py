import classes
import random
import methods as m

#character creation here
print('\n-- Guardians of Lothbrook --')
print("\nWelcome to the character creation!")
player_name = input('Enter your character name: ')
print(f'\nHello {player_name}!')
print("\nNow, select your player class ")

player_classes = ["Mage", "Paladin", "Warrior", "Ranger"]
print("Choose from the following classes:")
for i, c in enumerate(player_classes):
    print(f"{i+1}. {c}")

class_choice = input("Enter the number of your chosen class: ")
print('-------------------------------------------------------------------')
while not class_choice.isdigit() or int(class_choice) not in range(1, len(player_classes) + 1):
    class_choice = input("Invalid input. Please enter the number of your chosen class: ")
class_choice = int(class_choice)

if class_choice == 1:
    player = classes.mage()
elif class_choice == 2:
    player = classes.paladin()
elif class_choice == 3:
    player = classes.warrior()
else:
    player = classes.ranger()

print(f"\nWise choice! You have chosen to be a {player.class_name}; a mighty class worthy of these dungeons!")
print(f"Stats: \n|Attack| = {player.attack} \n|Magic| = {player.magic} \n|Defense| = {player.defense} \n|Resistance| = {player.resistance} \n|Speed| = {player.speed} \n|HP| = {player.hp}")

print(f'You have a {player.weaponName}. Good luck!')

# BATTLE PROMPT TESTING HERE!
print(f"\nTime for battle {player_name}, Your first enemy is approaching!")
print('-------------------------------------------------------------------')
monster = classes.monster()

battle = classes.Battle(player, monster)
battle.start_battle()

# After the battle, below is actually broken, just bc u can fail to flee and this will still print, so that needs to be fixed :)
print("\nReturning to the level menu. Great work.")
