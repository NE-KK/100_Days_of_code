# 100 Days of code by Angela Yu
# Day 5 - Password generator

from random import choice, shuffle
password = []

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "+", "*"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols would you like? "))


for _ in  range(0, nr_letters):
    password.append(choice(letters))

for _ in range(0, nr_numbers):
    password.append(choice(numbers))

for _ in range(0, nr_symbols):
    password.append(choice(symbols))


password_str = "".join(password)

shuffle(password)
password_shuffle_str = "".join(password)

print(password_str)
print(password_shuffle_str)