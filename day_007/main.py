# 100 Days of code by Angela Yu
# Day 7 - Hangman

from random import choice

word_list = ["aardvark", "baboon", "camel"]
blank_list = []

chosen_word = choice(word_list)
chosen_word_list = list(chosen_word)
print(f"Psst, it's {chosen_word}")

for letter in chosen_word:
    blank_list.append("_")


while "_" in blank_list:
    print(blank_list)

    guessed_letter = input("Guess a letter: ").lower()
    print(guessed_letter)

    if guessed_letter in chosen_word:
        for i in range(0, len(chosen_word_list)):
            if chosen_word_list[i] == guessed_letter:
                blank_list[i] = guessed_letter
        print(blank_list)
    else:
        print("Wrong")

