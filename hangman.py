import random

hangman_stages = ["""
    +------+
    |      |
           |
           |
           |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
           |
           |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
    |      |
           |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
   /|      |
           |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
   /|\     |
           |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
   /|\     |
   /       |
           |
           |
    ==============""", """
    +------+
    |      |
    O      |
   /|\     |
   / \     |
           |
           |
    =============="""]

play = True
words = []
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

fopen = open('C:\\Users\\clark\\Desktop\\Python\\wordlist.txt', "r")
for line in fopen:
    words.append(line.strip())

while play == True:
    miss = 0 
    win_word = words[random.randint(0, 850)]
    #print(win_word) #cheat
    wrd = []
    for char in win_word:
        wrd.append("_")
    already_guessed = []
    
    while miss != 6: 
        idx = []
        idxn = -1
        print(hangman_stages[miss], "\n")
        print(" ".join(wrd))
        print("\nGuessed Letters:", " ".join(already_guessed))
        ltr = input("\nGuess a letter: ")
        print("***************************************")
        
        if ltr in already_guessed:
            print("\nYou have already guessed that letter, try again!")
            continue
        if ltr.lower() not in alpha:
            print("Invalid choice. Please enter a single letter.")
            already_guessed.append(ltr)
            continue
        for letter in win_word:
            idxn += 1
            if letter == ltr.lower():
                idx.append(idxn)
        for i in idx:
            wrd[i] = ltr
        
        if "_" not in wrd:
            break
        if ltr.lower() not in win_word:
            miss += 1  
        already_guessed.append(ltr)
        
    if "_" not in wrd:
        print("Well done! The word was", "'" + win_word + "'!")
    if miss == 6:
        print(hangman_stages[miss])
        print("Too bad! The word was", "'" + win_word + "'!")
        
    choice = ""
    while choice != "yes" and choice != "no":
        choice = input("Play again? Enter 'yes' or 'no': ")
        if choice.lower() == "yes":
            play = True
        elif choice.lower() == "no":
            play = False
        else:
            print("Invalid input")
    print("***************************************")
