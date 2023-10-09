"""
PYTHON PROJECT #1: GUESS THE NUMBER
"""

# Used for random Number Generation
import random

# Allows for replay
play = True

# Game
while play == True:
    win_num = str(random.randint(1, 1000))
    guess = ""
    count = 0
    print("-----------------------------------")
    print("Welcome to my number guessing game!\nIn this game, you will try to guess a number of my choosing, with the number being between 1 and 1000!")
    play_again = ""

    while count == 0:
        try:
            count = int(input("How many max guesses would you like to have (Select a number greater than zero): "))
            print("-----------------------------------")
            if count == 0:
                print("Invalid choice. Please choose again.")
        except:
            print("-----------------------------------")
            print("Invalid choice. Please choose again.")

    print("Here we go!")
    guess = input("Guess a number: ")

    while guess != win_num and count >= 1:
            count -= 1
            if count == 0:
                continue
            print("-----------------------------------")
            if int(guess) < int(win_num): 
                print("Sorry! That guess is too low!")
            elif int(guess) > int(win_num):
                print("Sorry! That guess is too high!")

            if count == 1:
                guess = input("Guess again (You have " + str(count) + " guess left): ")
            else:
                guess = input("Guess again (You have " + str(count) + " guesses left): ")


    if count == 0:
        print("-----------------------------------")
        print("Sorry, you lose! The answer was " + win_num + "!")
    else:
        print("-----------------------------------")
        print("You win! The answer was " + win_num + "!")
    
    while play_again != "yes" and play_again != "no":
            play_again = input("Would you like to play again? Please enter 'yes' or 'no': ")
            if play_again == "yes":
                play = True
            elif play_again == "no":
                play = False
            else:
                print("-----------------------------------")
                print("Invalid choice. Please try again.")
                
# Exit Message
print("-----------------------------------")
print("Thanks for playing!")