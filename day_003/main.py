# 100 Days of code by Angela Yu
# Day 3 - Treasure Island

player_alive = True

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


if player_alive:
    decision_1 = input("You're on a crossroad, where do want to go? 'left' or 'right'. ")
    if decision_1 == "left":
        player_alive = True
    else:
        print("You fall into a hole. Game Over!")
        player_alive = False

if player_alive:
    decision_2 = input("You get to a big lake, wait or swim? ")
    if decision_2 == "wait":
        player_alive = True
    else:
        print("You get attacked by a trout. Game Over!")
        player_alive = False

if player_alive:
    decision_3 = input("You are suddenly in a room, which door do you choose? 'red', 'blue' or 'yellow'. ")
    if decision_3 == "yellow":
        print("You found the treasure")
        player_alive = True
    elif decision_3 == "red":
        print("You get burned by a fire. Game Over!")
        player_alive = False
    elif decision_3 == "blue":
        print("You get eaten by beasts.")
        player_alive = False
