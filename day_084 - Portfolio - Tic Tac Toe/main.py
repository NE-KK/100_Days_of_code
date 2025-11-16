# 100 Days of code by Angela Yu
# Day 84 - Professional Portfolio Project - Tic Tac Toe Game

game_still_going = True
game_is_won = False
player = "X"

field = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# functions -----------------------------------------------
def print_field(field):
    print(f"{field[0]} | {field[1]} | {field[2]}")
    print(f"{field[3]} | {field[4]} | {field[5]}")
    print(f"{field[6]} | {field[7]} | {field[8]}")


def choose_field(player):
    position = int(input("Choose a position from 1-9: ")) - 1
    
    if field[position] == "-":
        field[position] = player
        print_field(field)


def check_for_win(player):
    if (field[0] == player and field[1] == player and field[2] == player) or \
       (field[3] == player and field[4] == player and field[5] == player) or \
       (field[6] == player and field[7] == player and field[8] == player) or \
       (field[0] == player and field[3] == player and field[6] == player) or \
       (field[1] == player and field[4] == player and field[7] == player) or \
       (field[2] == player and field[5] == player and field[8] == player) or \
       (field[0] == player and field[4] == player and field[8] == player) or \
       (field[2] == player and field[4] == player and field[6] == player):
        return True
    else:
        return False


def check_for_fields(field):
    if "-" in field:
        return True
    else:
        return False    

def change_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


# game loop ------------------------------------------------
print_field(field)
while game_still_going:

    choose_field(player)
    game_is_won = check_for_win(player)
    fields_empty = check_for_fields(field)

    if game_is_won:
        game_still_going = False
        print(f"Player {player} won!")
    elif not fields_empty:
        game_still_going = False
        print("It's a tie!")
    else:
        player = change_player(player)
        continue
