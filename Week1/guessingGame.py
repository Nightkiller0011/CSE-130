# 1. Name:
#      Joshua Ellis
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This program is meant to be a guessing game. The user uses the Higher or Lower hints in order to guess the correct number.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      This program took me about two and a half hours to complete.

import random
# Intro to the game.
def main():
    
    restart = 1
    while(restart == 1):
        print(f"This is the \"Guess a number\" guessing game.\nYou try to guess a random number in the smallest number of attempts.") 
        game = 1
        count = 0
        # User chooses range of game.
        pick = int(input(f"Pick a positive interger: "))
        # Create the random number.
        number = random.randint(1,pick)
        # Create Array to store Guesses.
        guesslist = []
        # Enter the game loop.
        print(f"Guess a number between 1 and {pick}: ")
        while game == 1:
            # Prompt for users guess.
            guess = int(input(f"> "))
            # Compare number and guess, is it Too Low?
            if(number > guess & guess < pick):
                print(f"\tToo Low!")
                count += 1
                guesslist.append(guess)
            # Compare number and guess,is it Too High?
            elif(number < guess & guess < pick):
                print(f"\tToo High!")
                count += 1
                guesslist.append(guess)
            # Compare number and guess, is it Correct?
            elif(number == guess):
                count += 1
                guesslist.append(guess)
                print(f"\tGood Job! You managed to guess the number in {count} guesses! The numbers you guessed were {guesslist}.")
                game = 0
                # Asks user to play again.
                again = input(f"Do you want to restart?(y/n) ")
                if(again == "y"):
                    restart = 1
                else:
                    restart = 0
            # Is guess out of range?
            else:
                print(f"Please pick a number in range!")
main()
