# 100 Days of code by Angela Yu
# Day 11 - Project - Blackjack

# Rules:
# infinite card deck
# Jack/King/Queen count 10
# Ace count 11 or 1
# all cards have an equal prodability to be drawn
# cards are not removed from deck
# computer is dealer
from random import choice

def draw_card() -> int:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def print_decks(pd, cd):
    print(f"Player deck: {pd}; Sum: {sum(pd)}")
    print(f"Computer deck: {cd}; Sum: {sum(cd)}")


def ace_check_replace(card_deck: list):
    for i in range(len(card_deck)):
        if card_deck[i] == 11:
            card_deck[i] = 1
    
    return card_deck

def ask_for_game() -> bool:
    answer = input("Do you want to play Blackjack (y or n): ")
    if answer == "y":
        return True
    else:
        return False

def player_round(pd) -> list:
    round = True
    while round:
        answer = input("Type 'y' to get another card or 'n' to pass: ")
        
        if answer == "y":
            pd.append(draw_card())
            
            if sum(pd) > 21:
                pd = ace_check_replace(pd)

            print(f"Player deck: {pd}; current score: {sum(pd)}")
        else:
            round = False
        
    return pd

def computer_round(cd) -> list:
    round = True

    while round:
        sum_cards = sum(cd)

        if sum_cards < 17:
            cd.append(draw_card())
            if sum(cd) > 21:
                cd = ace_check_replace(cd)     
        else:
            round = False

    return cd


# main ----------------------------------------------------------------------------------
def main():

    run_game = ask_for_game()
  
    while run_game:
        # start decks
        player_deck = []
        computer_deck = []
        
        player_deck.append(draw_card())
        player_deck.append(draw_card())
        computer_deck.append(draw_card())

        if sum(player_deck) == 21:
            print("You won! Blackjack!")
            game_is_running = False
        else:
            game_is_running = True
        

        print(f"Player deck: {player_deck}; current score: {sum(player_deck)}")
        print(f"Computer: {computer_deck}")



        # player round --------------------------
        if game_is_running:
            player_deck = player_round(player_deck)
        
        if sum(player_deck) > 21:
            print("You lost!")
            print_decks(player_deck, computer_deck)
            game_is_running = False

        # computer round ------------------------
        if game_is_running:
            computer_deck = computer_round(computer_deck)
        
        if sum(computer_deck) > 21:
            print("You won!")
            print_decks(player_deck, computer_deck)
            game_is_running = False

        # result --------------------------------
        if game_is_running:
            if sum(player_deck) > sum(computer_deck):
                print("You won!")
                print_decks(player_deck, computer_deck)
            elif sum(player_deck) < sum(computer_deck):
                print("You lost!")
                print_decks(player_deck, computer_deck)
            else:
                print("A draw!")
                print_decks(player_deck, computer_deck)

        print("----------------------------------------")
        run_game = ask_for_game()

if __name__ == "__main__":
    main()
    print("Goodbye!")
