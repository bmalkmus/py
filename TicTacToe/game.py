
board = [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]]

def reset_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

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

    print([row_pos, col_pos])

    if (board[row_pos][col_pos] == " "):
        board[row_pos][col_pos] = "X"
        display_board()
    else:
        print("Position is already taken")
        user_choice()


user_choice()
