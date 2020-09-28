import random
import time


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
winner = False
Starter = "User"
turns = 0
replay = True

clear = "\n" * 100

def reset_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def display_board():
    print(" --- --- --- ")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print(" --- --- --- ")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print(" --- --- --- ")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print(" --- --- --- ")

def user_choice():
    row = ""
    row_choice=["TOP", "MIDDLE", "BOTTOM"]
    row_pos = None

    col = ""
    col_choice =["LEFT","CENTER","RIGHT"]
    col_pos = None

    while row not in row_choice:
        row = input("Select a row (TOP, MIDDLE, BOTTOM)").upper()
        if row not in row_choice:
            print("sorry that is not a correct selection")

    while col not in col_choice:
        col = input("Select a column (LEFT, CENTER, RIGHT)").upper()
        if col not in col_choice:
            print("sorry that is not a correct selection")

    if row == "TOP":
        row_pos=0
    elif row == "MIDDLE":
        row_pos=1
    else:
        row_pos=2

    if col == "LEFT":
        col_pos=0
    elif col == "CENTER":
        col_pos=1
    else:
        col_pos=2

    if (board[row_pos][col_pos] == " "):
        board[row_pos][col_pos] = "X"
        print(clear)
        display_board()
    else:
        print("Position is already taken")
        user_choice()

def computer_choice():

    def random_choice():
        options = [0, 1, 2]
        shufflable=options
        random.shuffle(shufflable)
        row = shufflable[0]
        random.shuffle(shufflable)
        col = shufflable[0]

        if (board[row][col] == " "):
                board[row][col] = "O"
        else:
            random_choice()

    print("hmmmmmmmm.....thinking....")
    time.sleep(2)
    random_choice()
    print(clear)
    display_board()

def check_win():
    
    s1 = board[0][0] == board[0][1] == board[0][2] != " "
    s2 = board[1][0] == board[1][1] == board[1][2] != " "
    s3 = board[2][0] == board[2][1] == board[2][2] != " "
    s4 = board[0][0] == board[1][0] == board[2][0] != " "
    s5 = board[0][1] == board[1][1] == board[2][1] != " "
    s6 = board[0][2] == board[1][2] == board[2][2] != " "
    s7 = board[0][0] == board[1][1] == board[2][2] != " "
    s8 = board[0][2] == board[1][1] == board[2][0] != " "
    
    if s1 or s2 or s3 or s4 or s5 or s6 or s7 or s8:
        print("There is a winner!!")
        return True
    else:
        return False

def turn ():
    if (Starter == "User"):
        user_choice()
        return "Computer"
    else:
        computer_choice()
        return "User"

def replay_game():
    response = ""
    replay_responses = ["Y", "N"]
    while response not in replay_responses:
        response = input("WOULD YOU LIKE TO REPLAY? (Y / N)").upper()
    if response == "Y":
        return True
    else:
        return False


while replay == True:
    reset_board()
    print(clear)
    display_board()
    while turns < 9 and winner == False:
        Starter = turn()
        winner = check_win()
        turns += 1

    if (winner == False and turns == 9):
        print("Appears to be a tie")

    replay = replay_game()

    

