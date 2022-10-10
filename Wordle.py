# File: Wordle.py

"""
William Hunter Nelson, Brandon Hunt, Euigun Jung, Brennan Williams, Jeff Hoather
Section 002
"""

from asyncio.windows_events import NULL
import random
import time
import subprocess


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():

    def winFunction(row):
        print("Congrats from the console!")

        #you won the game
        gw.show_message("That is correct!")
        print(gw._enter_listeners)
        # Remove the event listener for the enter key so that they can't try and more guesses 
        # after they win the game. They must restart the window to start over.
        gw._enter_listeners = []
        print(gw._enter_listeners)
        

    def get_guess(row):
        currentGuess = ''
        for i in range(5):
            currentLetter = gw.get_square_letter(row, i)
            #if currentLetter is blank, then don't add it to the currentGuess
            if currentLetter == ' ':
                currentGuess = currentGuess
            else:
                currentGuess += gw.get_square_letter(row, i)
        return currentGuess

    def enter_action(s):

        #this needs to be incremented after each guess that meets the criteria (5 letters, in the dictionary)
        currentGuess = get_guess(gw.get_current_row())
        currentGuess= currentGuess.lower()
        
        #get current length, if it's not 5 then break out of this function and don't increment the row
        if len(currentGuess) == 5:

            #check if lower case word is in the dictionary, if not, show message saying word is not in dictionary
            if currentGuess.lower() in FIVE_LETTER_WORDS:
                
                # if word is correct


                #guess logic 
                wordToGuessList = list(wordToGuess)
                print(wordToGuessList)
                # main loop to check each letter in guess
                print(currentGuess)
                for i in range(len(currentGuess)):
                    letter = currentGuess[i]
                    print(letter)
                    if letter in wordToGuessList:

                        # Setting letters yellow as default color
                        gw.set_square_color(gw.get_current_row(),i,"#CCBB66")
                        gw.set_key_color(letter.upper(),PRESENT_COLOR)
                        # if (gw.get_key_color(letter.upper()) != CORRECT_COLOR):
                    
                        if wordToGuess[i] == letter:
                            gw.set_square_color(gw.get_current_row(),i,"#66BB66")
                            gw.set_key_color(letter.upper(),CORRECT_COLOR)

                        #else, color gray
                    else:
                        gw.set_square_color(gw.get_current_row(),i,"#999999")
                        gw.set_key_color(letter.upper(),"#999999")

                # Check our win condition
                if currentGuess.lower() == wordToGuess:
                    winFunction("row")
                    # time.sleep(5)
                    # exit()
                    # r = subprocess.run(['echo', 'hello timeout'], timeout=5)
                    # exit()
                    # try:
                    #     r = subprocess.run(['ping', 'www.google.com'], timeout=5)
                    # except subprocess.TimeoutExpired as e:
                    #     print(e)
                else:
                    # If they didn't win, increment current row
                    if (gw.get_current_row() == 5):
                        print('end')
                        gw.show_message(("So close! The word was: "+ wordToGuess))

                    gw.set_current_row(gw.get_current_row() + 1)
                
            else:
                gw.show_message("Word not in dictionary")              

        else:
            gw.show_message("You must enter a 5 letter word")
    

    # On game start select a random word from our word list
    randIndex = random.randint(0, len(FIVE_LETTER_WORDS))
    wordToGuess = FIVE_LETTER_WORDS[randIndex]
    print(wordToGuess)
    gw = WordleGWindow()
    gw.show_message("Enter your guess!")
    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()
