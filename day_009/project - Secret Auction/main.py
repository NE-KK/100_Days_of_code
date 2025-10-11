# 100 Days of code by Angela Yu
# Day 9 - Secret Auction

import os

auction_dict = {}
place_bet = True
max_bid = 0
max_bidder = ""


while place_bet:
    name = input("Type your name?: ")
    price = int(input("What is your bet?: "))
    
    os.system('cls')

    auction_dict[name] = price

    next_bid = input("Another bid? y/n: ")

    if next_bid == "n":
        place_bet = False

# print(auction_dict)

for name in auction_dict:
    if auction_dict[name] > max_bid:
        max_bid = auction_dict[name]
        max_bidder = name

print(f"The auction won {max_bidder}, with ${max_bid}.")
