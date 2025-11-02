# 100 Days of code by Angela Yu
# Day 12 - Number guessing

from random import randint


def set_difficulty() -> int:
    difficulty_level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return 10
    else:
        return 5   


def main():
    game_won = False

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    searched_number = randint(1, 101)
    # for debuging ------------------------------ 
    print(f"psst, it's {searched_number}")

    attemps = set_difficulty()



    while attemps > 0:
        print(f"{attemps} attemps remaining to guess the number.")
        guess = int(input("Guess a number: "))

        if guess > searched_number:
            print(f"{guess} is to high. Try again!")
        elif guess < searched_number:
            print(f"{guess} is to low. Try again!")
        else:
            game_won = True
            break

        attemps -= 1

    if game_won:
        print(f"You found {searched_number}. You won.")
    else:
        print(f"{searched_number} was searched. Better luck next time.")

if __name__ == "__main__":
    main()
