# Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending
# on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game.
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

# import random  
# set_of_choices = set(["left", "right", "far right", "look around", "fight", "leave", "inventory"])
# inventory= []
# user_attack = random.randint(4, 8)
# user_defense = 8
# user_health = 10
# goblin_attack = random.randint(1, 3)
# goblin_defense = 4
# goblin_health = 2
# ogre_attack = random.randint(3, 8)
# ogre_defense = 12
# ogre_health = 6
# dragon_attack = random.randint(10, 12)
# dragon_defense = 20
# dragon_health = 10
# items = {"sword": 5, "potion": 2, "golden_axe": 8, "rusty_dagger": 3}
# user_name = input("To get started, please enter your name: ")
# print(f"Hello {user_name} Welcome to Echoes of the Keep!")
# door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()
# while user_health > 0:
     
#     if door_choice == "left":
#         print("You have entered an empty-looking room")
#         look_around = input("Would you like to look around? yes / no: ").lower()
#         if look_around == "yes":
#             print("You have found a secret latch in the floor if the room. You open the latch, it contains a sword!")
#             sword_choice = input("Would you like to take the sword: yes / no: ").lower()
#             if sword_choice == "yes":
#                 inventory.append(sword)
#                 print("You now have a sword!")
#                 print("You have returned to the castle lobby")
#                 print(inventory)
#                 input("Would you like to use an item from your inventory? yes / no: ").lower()
#                 input("Which item would you like to use?").lower()
#                 inventory.remove()
#             else: 
#                 print("You have left the sword")
#         else: 
#             print("You have left the room without looking around")
#             print("You have returned to the castle lobby")
#             print(inventory)
#             input("Would you like to use an item from your inventory? yes / no: ").lower()
#             input("Which item would you like to use?").lower()
#             door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()

#     elif door_choice == "far left":
#         print("You have entered the room with a chest!")
#         print("You walk towards the chest and an ogre jumps out and charges at you!")
#         print("You attack the ogre!. You dodge its blow and strike first. ")
#         ogre_health -= user_attack
#         print(f"The ogre has {ogre_health} health left.")
#         print("The ogre attacks you! You block the blow and counterattack!")
#         user_health -= ogre_attack
#         print(f"You have {user_health} health left.")
#         print("You attack the ogre!")
#         ogre_health -= user_attack
#         print("You have defeated the ogre!")
#         print("You open the chest and find a potion!")
#         print("You have added the potion to your inventory!")
#         inventory.append(potion)
#         print("You have returned to the castle lobby")
#         print(inventory)
#         door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()
#     elif door_choice == " far right":
#         print(" You have entered a room with nothing but two armoirs in the corner")
#     open_large_armoir = input("You have entered a room with nothing but two armoirs in the corner. Would you like to open the large armoir? yes / no: ").lower()
#     if open_large_armoir == "yes":
#             print("You have found a golden axe!")
#             axe_choice = input("Would you like to take the golden axe? yes / no: ").lower()
#             if axe_choice == "yes":
#                 inventory.append(golden_axe)
#                 print("You now have a golden axe!")
#             else: 
#                 print("You have left the axe")
#     open_small_armoir = input("Would you like to open the small armoir? yes / no: ").lower()
#     if open_small_armoir == "yes":
#             print("A goblin attacks!")
#             print(f"You attack the goblin!. You dodge its blow and strike first. You hit the goblin for 5 damage!")
#             goblin_health -= user_attack
#             print("You have defeated the goblin!")
#     dagger_choice = input("The goblin dropped a rusty dagger. Would you like to like to add the rusty dagger to inventory? yes / no: ")
#     if dagger_choice == "yes":
#         inventory.append("dagger")
#         print("You now have a rusty dagger!")
#     else:
#         print("You have left the rusty dagger") 
#     print("You have returned to the castle lobby")
#     print(inventory)
#     input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()
    
#     elif door_choice == "right":
#     print("You have entered the room with a dragon!")
#     fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
#     if fight_choice == "yes":
#     if golden_axe in inventory:
#                 print("You bravely fight the dragon with your axe and win! You are victorious!")
#         else:
#                 print("You try to fight the dragon, but without a golden axe, you are eaten. Game over.")
#     elif fight_choice == "no":
#             has_inventory = False
#             print("You chose not to fight the dragon. You lose.")

#         else:
#             print("You chose not to fight the dragon. You lose.")
#     else: 
#         print("Invalid choice. You lose.")


        
import random

# Define possible choices
set_of_choices = set(["left", "right", "far left", "far right", "look around", "fight", "leave", "inventory"])
inventory = []

# Define items with integer values for their effect (e.g., attack or defense power)
items = {"sword": 5, "golden axe": 10, "shield": 3,"potion": 15}
# Player stats
user_attack = random.randint(4, 8)
user_defense = 8
user_health = 10
# Enemy stats
goblin_attack = random.randint(1, 3)
goblin_defense = 4
goblin_health = 2

user_name = input("To get started, please enter your name: ")
print(f"Hello {user_name}! Welcome to Echoes of the Keep!")
door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()

while user_health > 0:
    if door_choice == "left":
        print("You have entered an empty-looking room.")
        look_around = input("Would you like to look around? yes / no: ").lower()
        if look_around == "yes":
            print("You have found a secret latch containing a sword!")
            sword_choice = input("Would you like to take the sword? yes / no: ").lower()
            if sword_choice == "yes":
                inventory.append("sword")
                print(f"You now have a sword! (Attack Power: {items['sword']})")
            else:
                print("You have left the sword.")
        print("You have returned to the castle lobby.")

    elif door_choice == "far left":
        print("You enter a room with a chest and are ambushed by an ogre!")
        user_health -= goblin_attack
        if user_health > 0:
            print("You defeated the ogre and found a potion in the chest.")
            inventory.append("potion")
            print(f"You now have a potion! (Health Boost: {items['potion']})")
        print("You have returned to the castle lobby.")

    elif door_choice == "far right":
        print("You enter a room with two armoires.")
        open_large_armoire = input("Open the large armoire? yes / no: ").lower()
        if open_large_armoire == "yes":
            print("You have found a golden axe!")
            if input("Take the golden axe? yes / no: ").lower() == "yes":
                inventory.append("golden axe")
                print(f"You now have a golden axe! (Attack Power: {items['golden axe']})")
        open_small_armoire = input("Open the small armoire? yes / no: ").lower()
        if open_small_armoire == "yes":
            print("A goblin attacks!")
            goblin_health -= user_attack
            print("You defeated the goblin! It dropped a rusty dagger.")
            if input("Take the dagger? yes / no: ").lower() == "yes":
                inventory.append("dagger")
                print("You now have a rusty dagger!")

    elif door_choice == "right":
        print("You have entered a room with a dragon!")
        fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
        if fight_choice == "yes":
            if "golden axe" in inventory:
                print(f"You bravely fight the dragon with your golden axe (Attack Power: {items['golden axe']}) and win! You are victorious!")
            else:
                print("Without a golden axe, you are defeated by the dragon. Game over.")
                break
        else:
            print("You chose not to fight the dragon. You lose.")
            break
    else:
        print("Invalid choice.")

    door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower()
