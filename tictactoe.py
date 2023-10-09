
board = [[" ", "|", " ", "|", " "], 
         ["-", "+", "-", "+", "-"], 
         [" ", "|", " ", "|", " "], 
         ["-", "+", "-", "+", "-"], 
         [" ", "|", " ", "|", " "]]
turn = "X"

def prntboard():
    for row in board:
        print("".join(row))

def turnswap():
    global turn
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
        
def victory():
    if (board[0][0] == turn and board[0][2] == turn and board[0][4] == turn) or (board[0][0] == turn and board[2][0] == turn and board[4][0] == turn) or (board[0][2] == turn and board[2][2] == turn and board[4][2] == turn) or (board[0][4] == turn and board[2][4] == turn and board[4][4] == turn) or (board[2][0] == turn and board[2][2] == turn and board[2][4] == turn) or (board[4][0] == turn and board[4][2] == turn and board[4][4] == turn) or (board[0][0] == turn and board[2][2] == turn and board[4][4] == turn) or (board[0][4] == turn and board[2][2] == turn and board[4][0] == turn):
        print(turn, "wins!")
        return True
    else:
        return False
        
prntboard()
spaces = 9
while spaces > 0:
    row = input("Choose a row: ")
    clm = input("Choose a column: ")
    if row == "1" and clm == "1":
        if board[0][0] != " ":
            print("That space is occupied. Try again.")
            continue
        board[0][0] = turn
    elif row == "1" and clm == "2":
        if board[0][2] != " ":
            print("That space is occupied. Try again.")
            continue
        board[0][2] = turn
    elif row == "1" and clm == "3":
        if board[0][4] != " ":
            print("That space is occupied. Try again.")
            continue
        board[0][4] = turn
    elif row == "2" and clm == "1":
        if board[2][0] != " ":
            print("That space is occupied. Try again.")
            continue
        board[2][0] = turn
    elif row == "2" and clm == "2":
        if board[2][2] != " ":
            print("That space is occupied. Try again.")
            continue
        board[2][2] = turn
    elif row == "2" and clm == "3":
        if board[2][4] != " ":
            print("That space is occupied. Try again.")
            continue
        board[2][4] = turn
    elif row == "3" and clm == "1":
        if board[4][0] != " ":
            print("That space is occupied. Try again.")
            continue
        board[4][0] = turn
    elif row == "3" and clm == "2":
        if board[4][2] != " ":
            print("That space is occupied. Try again.")
            continue
        board[4][2] = turn
    elif row == "3" and clm == "3":
        if board[4][4] != " ":
            print("That space is occupied. Try again.")
            continue
        board[4][4] = turn
    else:
        print("That is not a valid space. Try again.")
        continue
    if victory() == True:
        break
    spaces -= 1
    turnswap()
    prntboard()
    if spaces == 0:
        print("It's a tie!")
print("Thanks for playing!")