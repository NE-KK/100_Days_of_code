# 100 Days of code by Angela Yu
# Day 14 - Higher Lower Game

from art import logo, vs
from game_data import data
from random import choice
import os

def random_data():
    return choice(data)

def text_format(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def num_follower(account):
    return account['follower_count']


# Game starting values
score = 0
game_continue = True
choice_a = random_data()
choice_b = random_data()


while game_continue:
    # os.system('clear')
    print(logo)

    follower_a = num_follower(choice_a)
    print(f"Compare A: {text_format(choice_a)}")

    print(vs)

    follower_b = num_follower(choice_b)
    print(f"Against B: {text_format(choice_b)}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (follower_a > follower_b and user_choice == 'A') or (follower_b > follower_a and user_choice == 'B'):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
    
    choice_a = choice_b
    choice_b = random_data()

