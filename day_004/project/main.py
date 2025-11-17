# 100 Days of code by Angela Yu
# Day 4 - Project - Rock, Paper, Scissors

import art
from random import random
from math import floor


def find_symbol(choice):
    if choice == 0:
        return art.rock
    elif choice == 1:
        return art.paper
    elif choice == 2:
        return art.scissors


def evaluate_winner(player, computer):
    if player == computer:
        return "It's a draw"
    elif player == 0 and computer == 2:
        return "You win!"
    elif player == 1 and computer == 0:
        return "You win!"
    elif player == 2 and computer == 1:
        return "You win!"
    else:
        return "You lose"
    

player_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = floor(random() * 3)

player_symbol = find_symbol(player_choice)
print(player_symbol)

print("Computer chose:")
computer_symbol = find_symbol(computer_choice)
print(computer_symbol)

result = evaluate_winner(player_choice, computer_choice)
print(result)
