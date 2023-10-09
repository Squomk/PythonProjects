import random

board = [[" ", "|", " ", "|", " "], 
         ["-", "+", "-", "+", "-"], 
         [" ", "|", " ", "|", " "], 
         ["-", "+", "-", "+", "-"], 
         [" ", "|", " ", "|", " "]]
 
def token_choice():
    tkn = ""
    while tkn != "x" and tkn != "o":
        tkn = input("Would you like to be Xs or Os? Enter 'x' or 'o': ")
        if tkn == "x":
            return "X"
        elif tkn == "o":
            return "O"
        else:
            input("Invalid choice. Please type 'x' or 'o'.")

def coin():
    flip = 999
    while flip != 0 and flip != 1: 
        flip = input("Let's flip a coin to see who goes first. Enter 'heads' or 'tails': ")
        if flip == "heads":
            flip = 1
        elif flip == "tails":
            flip = 0
        else:
            print("Invalid choice. Please type 'heads' or 'tails'.")
            
    toss = random.randint(0, 1) #comment out for autowin
    #toss = 1 #comment in to end autowin
    if toss == 1:
        print("Heads wins!")
    elif toss == 0:
        print("Tails wins!")
    if toss == flip:
        print("You go first!")
        return 1
    else:
        print("I go first!")
        return 2

ai = ""
order = coin() 
player = token_choice()   
if player == "X":
    ai = "O"
elif player == "O":
    ai = "X"
        

def prntboard():
    for row in board:
        print("".join(row))    
        
def victory(turn):
    if (board[0][0] == turn and board[0][2] == turn and board[0][4] == turn) or (board[0][0] == turn and board[2][0] == turn and board[4][0] == turn) or (board[0][2] == turn and board[2][2] == turn and board[4][2] == turn) or (board[0][4] == turn and board[2][4] == turn and board[4][4] == turn) or (board[2][0] == turn and board[2][2] == turn and board[2][4] == turn) or (board[4][0] == turn and board[4][2] == turn and board[4][4] == turn) or (board[0][0] == turn and board[2][2] == turn and board[4][4] == turn) or (board[0][4] == turn and board[2][2] == turn and board[4][0] == turn):
        print("***************************************")
        prntboard()
        print(turn, "wins!")
        return True
    else:
        return False
        

def player_turn(spaces):
    turn = player
    while turn == player:
        print("***************************************")
        prntboard()
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
        turn = 0  


def ai_turn(spaces):
    turn = ai
    idx = [0, 2, 4] 
    row = 9
    clm = 9
    ok = False
    if spaces == 9:
        row = random.choice(idx)
        clm = random.choice(idx)
        board[row][clm] = turn
    if spaces == 8:
        while ok == False:
            row = random.choice(idx)
            clm = random.choice(idx)
            if board[row][clm] != " ":
                continue
            elif board[row][clm] == " ":
                board[row][clm] = turn
            ok = True
    if spaces < 8:
        #win scenarios
        if board[0][0] == ai and board[0][4] == ai and board[0][2] == " ":
            board[0][2] = ai
        elif board[0][0] == ai and board[4][4] == ai and board[2][2] == " ":
            board[2][2] = ai
        elif board[0][0] == ai and board[4][0] == ai and board[2][0] == " ":
            board[2][0] = ai
        elif board[0][2] == ai and board[4][2] == ai and board[2][2] == " ":
            board[2][2] = ai
        elif board[4][0] == ai and board[0][4] == ai and board[2][2] == " ":
            board[2][2] = ai
        elif board[4][0] == ai and board[4][4] == ai and board[4][2] == " ":
            board[4][2] = ai 
        elif board[2][0] == ai and board[2][4] == ai and board[2][2] == " ":
            board[2][2] = ai
        elif board[0][0] == ai and board[0][2] == ai and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][2] == ai and board[0][4] == ai and board[0][0] == " ":
            board[0][0] = ai
        elif board[2][0] == ai and board[2][2] == ai and board[2][4] == " ":
            board[2][4] = ai
        elif board[2][2] == ai and board[2][4] == ai and board[2][0] == " ":
            board[2][0] = ai
        elif board[4][0] == ai and board[4][2] == ai and board[4][4] == " ":
            board[4][4] = ai
        elif board[4][2] == ai and board[4][4] == ai and board[4][0] == " ":
            board[4][0] = ai
        elif board[0][0] == ai and board[2][0] == ai and board[4][0] == " ":
            board[4][0] = ai
        elif board[2][0] == ai and board[4][0] == ai and board[0][0] == " ":
            board[0][0] = ai
        elif board[0][2] == ai and board[2][2] == ai and board[4][2] == " ":
            board[4][2] = ai
        elif board[2][2] == ai and board[4][2] == ai and board[0][2] == " ":
            board[0][2] = ai
        elif board[0][4] == ai and board[2][4] == ai and board[4][4] == " ":
            board[4][4] = ai
        elif board[2][4] == ai and board[4][4] == ai and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][0] == ai and board[2][2] == ai and board[4][4] == " ":
            board[4][4] = ai
        elif board[2][2] == ai and board[4][4] == ai and board[0][0] == " ":
            board[0][0] = ai
        elif board[0][4] == ai and board[2][2] == ai and board[4][0] == " ":
            board[4][0] = ai
        elif board[4][0] == ai and board[2][2] == ai and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][4] == ai and board[4][4] == ai and board[2][4] == " ":
            board[2][4] = ai
        #Block conditions
        elif board[0][0] == player and board[0][4] == player and board[0][2] == " ":
            board[0][2] = ai
        elif board[0][0] == player and board[4][4] == player and board[2][2] == " ":
            board[2][2] = ai
        elif board[0][0] == player and board[4][0] == player and board[2][2] == " ":
            board[2][0] = ai
        elif board[0][2] == player and board[4][2] == player and board[2][2] == " ":
            board[2][2] = ai
        elif board[4][0] == player and board[0][4] == player and board[2][2] == " ":
            board[2][2] = ai
        elif board[4][0] == player and board[4][4] == player and board[4][2] == " ":
            board[4][2] = ai
        elif board[2][0] == player and board[2][4] == player and board[2][2] == " ":
            board[2][2] = ai
        elif board[0][0] == player and board[0][2] == player and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][2] == player and board[0][4] == player and board[0][0] == " ":
            board[0][0] = ai
        elif board[2][0] == player and board[2][2] == player and board[2][4] == " ":
            board[2][4] = ai
        elif board[2][2] == player and board[2][4] == player and board[2][0] == " ":
            board[2][0] = ai
        elif board[4][0] == player and board[4][2] == player and board[4][4] == " ":
            board[4][4] = ai
        elif board[4][2] == player and board[4][4] == player and board[4][0] == " ":
            board[4][0] = ai
        elif board[0][0] == player and board[2][0] == player and board[4][0] == " ":
            board[4][0] = ai
        elif board[2][0] == player and board[4][0] == player and board[0][0] == " ":
            board[0][0] = ai
        elif board[0][2] == player and board[2][2] == player and board[4][2] == " ":
            board[4][2] = ai
        elif board[2][2] == player and board[4][2] == player and board[0][2] == " ":
            board[0][2] = ai
        elif board[0][4] == player and board[2][4] == player and board[4][4] == " ":
            board[4][4] = ai
        elif board[2][4] == player and board[4][4] == player and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][0] == player and board[2][2] == player and board[4][4] == " ":
            board[4][4] = ai
        elif board[2][2] == player and board[4][4] == player and board[0][0] == " ":
            board[0][0] = ai
        elif board[0][4] == player and board[2][2] == player and board[4][0] == " ":
            board[4][0] = ai
        elif board[4][0] == player and board[2][2] == player and board[0][4] == " ":
            board[0][4] = ai
        elif board[0][4] == player and board[4][4] == player and board[2][4] == " ":
            board[2][4] = ai
        else:
            while ok == False:
                row = random.choice(idx)
                clm = random.choice(idx)
                if board[row][clm] != " ":
                    continue
                elif board[row][clm] == " ":
                    board[row][clm] = turn
                ok = True
    
    
if order == 1:
    spaces = 9
    while spaces > 0:
        player_turn(spaces)
        win = victory(player)
        if win == True:
            break
        spaces -= 1
        if spaces == 0:
            print("It's a tie!")
            break
        ai_turn(spaces)
        win = victory(ai)
        if win == True:
            break
        spaces -= 1
elif order == 2:
    spaces = 9
    while spaces > 0:
        ai_turn(spaces)
        win = victory(ai)
        if win == True:
            break
        spaces -= 1
        if spaces == 0:
            print("It's a tie!")
            break
        player_turn(spaces)
        win = victory(player)
        if win == True:
            break
        spaces -= 1
    
print("Thanks for playing!")