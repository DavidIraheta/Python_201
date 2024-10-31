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

import random  
set_of_choices = {"left", "right", "look around", "fight", "leave", "inventory"}
item_inventory= []
user_name = input("What is your name?: ")
print(f"Hello {user_name} Welcome to Medieval Times")
print("There are two doors in front of you. One on the left and one on the right")
has_sword = False
has_inventory = True
door_choice = input("Which door do you choose, left or right?: ").lower()
if door_choice == "left":
    print("You have entered an empty room")
    look_around = input("Would you like to look around? yes / no: ").lower()
    if look_around == "yes":
        print("You have found a sword!")
        sword_choice = input("Would you like to take the sword: yes / no: ").lower()
        if sword_choice == "yes":
            has_sword = True
            print("You now have a sword!")
        else: 
            print("You have left the sword")
    else: 
        print("You have left the room without looking around")
    open_right_door  = input("Would you like to open the right door now? yes / no: ").lower()
    if open_right_door == "yes":
        print("You have entered the room with a dragon!")
        fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
        if fight_choice == "yes":
            if has_sword:
                print("You bravely fight the dragon with your sword and win! You are victorious!")
            else:
                print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
        else:
            print("You chose not to fight the dragon. You lose.")
elif door_choice == "right":
    print("You have entered the room with a dragon!")
    fight_choice = input("Would you like to fight the dragon? yes / no: ").lower()
    if fight_choice == "yes":
        if has_sword:
            print("You bravely fight the dragon with your sword and win! You are victorious!")
        else:
            print("You try to fight the dragon, but without a sword, you are eaten. Game over.")
    elif fight_choice == "no":
        has_inventory = False
        print("You chose not to fight the dragon. You lose.")

    else:
        print("You chose not to fight the dragon. You lose.")
else: 
    print("Invalid choice. You lose.")

    